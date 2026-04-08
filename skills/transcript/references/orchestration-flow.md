# Orchestration Flow

> Extracted from `skills/transcript/SKILL.md` for progressive disclosure (Level 3).
> **Parent:** `skills/transcript/SKILL.md` § Orchestration Flow

## Document Sections

| Section | Purpose |
|---------|---------|
| [Step-by-Step Pipeline](#l1-step-by-step-pipeline-v20-hybrid) | 4-step pipeline with error handling |
| [State Passing](#l2-state-passing-between-agents-v20) | State keys and YAML schemas |

---

## L1: Step-by-Step Pipeline (v2.0 Hybrid)

```
STEP 1: PARSE + CHUNK (ts-parser v2.0)
──────────────────────────────────────
Input:  Raw transcript file (VTT/SRT/TXT)
Process:
  1. Detect format (VTT header check)
  2. IF VTT:
     - Delegate to Python parser (Bash tool)
     - Validate output schema
     - Chunk to 500-segment files
  3. ELSE (SRT/TXT):
     - Use LLM parsing (fallback)
     - Chunk if large file
Output: index.json + chunks/chunk-NNN.json
Errors: Python failure → fallback to LLM parsing

STEP 2: EXTRACT (ts-extractor)
──────────────────────────────
Input:  index.json + chunks/*.json (NEVER canonical-transcript.json)
Process:
  1. Read index.json for metadata and chunk listing
  2. Process each chunk sequentially for entity extraction
  3. Extract entities with confidence scores and citations
Output: extraction-report.json
Errors: Low confidence extractions → flag for review

STEP 3: FORMAT (ts-formatter)
─────────────────────────────
Input:  index.json + extraction-report.json (NEVER canonical-transcript.json)
Output: packet/ directory (8 files per ADR-002)
Errors: Token overflow → split files automatically (ADR-004)

STEP 3.5: MINDMAP GENERATION (ts-mindmap-*, conditional - ADR-006)
──────────────────────────────────────────────────────────────────
Condition: --no-mindmap flag NOT set (mindmaps ON by default)
Input:  ts_extractor_output.extraction_report_path + ts_formatter_output.packet_path
Process:
  1. IF --no-mindmap flag is NOT set:  # Default behavior
     - IF --mindmap-format == "mermaid" OR "both" (default):
       Invoke ts-mindmap-mermaid
       Output: 08-mindmap/mindmap.mmd
     - IF --mindmap-format == "ascii" OR "both" (default):
       Invoke ts-mindmap-ascii
       Output: 08-mindmap/mindmap.ascii.txt
  2. ELSE:
     - Skip mindmap generation (user opted out)
     - ts_mindmap_output.overall_status = "skipped"
Output: ts_mindmap_output state key
Errors: Graceful degradation - continue with warning, provide regeneration instructions

STEP 4: REVIEW (ps-critic)
──────────────────────────
Input:  All generated files
Output: quality-review.md
Errors: Score < 0.90 → report issues for human review
```

## L2: State Passing Between Agents (v2.0)

> **PURPOSE:** State keys provide persistence across agent boundaries, enabling:
> - **Error recovery** - Agents can resume from last checkpoint
> - **Debugging** - Full pipeline trace in state history
> - **Quality assurance** - ps-critic validates entire pipeline state

| Agent | Output Key | Passed To | Purpose |
|-------|------------|-----------|---------|
| ts-parser v2.0 | `ts_parser_output` | ts-extractor | Parsing results + chunk metadata |
| ts-extractor | `ts_extractor_output` | ts-formatter | Extraction report + stats |
| ts-formatter | `ts_formatter_output` | ts-mindmap-*, ps-critic | Packet location + file manifest |
| ts-mindmap-* | `ts_mindmap_output` | ps-critic | Mindmap paths + generation status |
| ps-critic | `quality_output` | User/Orchestrator | Quality validation results |

### State Schema (v2.0)

```yaml
ts_parser_output:
  canonical_json_path: string          # Full transcript JSON (archive only, ~930KB)
  index_json_path: string              # Chunk index metadata (~8KB)
  chunks_dir: string                   # chunks/ directory path
  chunk_count: integer                 # Number of chunk files created
  format_detected: vtt|srt|plain       # Auto-detected or forced format
  parsing_method: python|llm           # Strategy Pattern routing decision
  segment_count: integer               # Total segments in transcript
  speaker_count: integer               # Unique speakers identified
  duration_ms: integer|null            # Transcript duration (null for plain text)
  validation_passed: boolean           # Schema validation result
  warnings: string[]                   # Non-fatal parsing issues
  errors: string[]                     # Fatal errors (if any)
  fallback_triggered: boolean          # True if Python→LLM fallback occurred

ts_extractor_output:
  extraction_report_path: string       # Path to extraction-report.json (~35KB)
  action_count: integer                # len(action_items) - MANDATORY consistency
  decision_count: integer              # len(decisions) - MANDATORY consistency
  question_count: integer              # len(questions) - MANDATORY consistency
  topic_count: integer                 # len(topics) - MANDATORY consistency
  speaker_count: integer               # len(speakers) - MANDATORY consistency
  high_confidence_ratio: float         # Ratio of high-confidence extractions
  average_confidence: float            # Mean confidence across all entities
  chunks_processed: integer            # Number of chunks analyzed
  input_format: "chunked"|"single_file" # Input format used
  tier_1_count: integer                # Rule-based extractions (high confidence)
  tier_2_count: integer                # ML-based extractions (medium confidence)
  tier_3_count: integer                # LLM-based extractions (variable confidence)

ts_formatter_output:
  packet_path: string                  # Directory path to 8-file packet
  files_created: string[]              # List of all created files
  split_files: integer                 # Number of files split due to token limits
  total_tokens: integer                # Sum of tokens across all files
  max_file_tokens: integer             # Largest file token count
  anchor_count: integer                # Total anchors in registry
  backlink_count: integer              # Total backlinks generated
  all_files_under_limit: boolean       # True if all < 35K tokens per ADR-004

ts_mindmap_output:
  enabled: boolean                      # Was --no-mindmap NOT set?
  format_requested: string              # "mermaid" | "ascii" | "both"
  mermaid:
    path: string | null                 # Path to 08-mindmap/mindmap.mmd
    status: string                      # "complete" | "failed" | "skipped"
    error_message: string | null
    topic_count: integer
    deep_link_count: integer
    syntax_validated: boolean
  ascii:
    path: string | null                 # Path to 08-mindmap/mindmap.ascii.txt
    status: string                      # "complete" | "failed" | "skipped"
    error_message: string | null
    topic_count: integer
    max_line_width: integer             # Should be <= 80
    box_drawing_valid: boolean
  overall_status: string                # "complete" | "partial" | "failed" | "skipped"
  regeneration_command: string | null

quality_output:
  quality_score: float                  # Aggregate score (0.0-1.0)
  passed: boolean                       # True if >= quality_threshold (default 0.90)
  issues: string[]                      # Quality gate failures
  recommendations: string[]             # Improvement suggestions
  criteria_scores: dict                 # Per-criterion scores
  mindmap_criteria_applied: boolean     # True if MM-*/AM-* criteria checked
  artifacts_validated: string[]         # List of files checked
  validation_timestamp: string          # ISO 8601 timestamp
```

---

> Error state structures and recovery documentation: see [error-handling.md](error-handling.md)
