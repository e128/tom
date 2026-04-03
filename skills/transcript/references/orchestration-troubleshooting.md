# Orchestration Troubleshooting (F-005)

> Reference documentation for transcript skill pipeline troubleshooting. Loaded on demand from SKILL.md.
> Covers: Pipeline stuck states, agent timeouts, quality gate failures, file conflicts, mindmap failures, state mismatches, parser fallback issues.

---

### Orchestration Troubleshooting (F-005)

> **PURPOSE:** Diagnose and resolve pipeline orchestration failures.
> Use this section when the skill appears "stuck" or agents aren't executing in sequence.

---

#### Issue: Pipeline Stuck After ts-parser

**Symptom:**
```
ts-parser completed successfully
Status: ts_parser_output.validation_passed = true
Expected: ts-extractor should start automatically
Actual: No activity, pipeline appears frozen
```

**Diagnostic Steps:**

1. **Check state propagation:**
```bash
# Verify ts_parser_output state key exists
cat /output/.skill-state.json | jq '.ts_parser_output'
```

2. **Verify required files exist:**
```bash
ls -lh /output/index.json
ls -lh /output/chunks/
```

3. **Check for blocking errors:**
```bash
cat /output/.skill-state.json | jq '.ts_parser_output.errors'
```

**Resolution:**

**If state key missing:**
```bash
# Orchestration bug - restart from parsing
uv run tom transcript parse <file> --output-dir /output/
```

**If files missing despite validation_passed = true:**
```bash
# File persistence violation (P-002) - report as bug
uv run tom transcript debug --validate-persistence /output/
```

**If errors[] is non-empty despite status = "success":**
```bash
# State inconsistency - force re-run extraction
uv run tom transcript resume --from extraction --force
```

---

#### Issue: Agent Timeout During Extraction

**Symptom:**
```
ts-extractor started processing chunks
Progress: 8/15 chunks processed
Error: Agent timeout after 300 seconds
```

**Diagnostic Steps:**

1. **Check chunk sizes:**
```bash
du -h /output/chunks/*.json
# Look for chunks > 200KB (may exceed token limits)
```

2. **Check partial extraction report:**
```bash
ls -lh /output/extraction-report.json
# File may exist but be incomplete
```

3. **Estimate remaining time:**
```bash
# Average 30-40 seconds per chunk for large chunks
# Remaining: (15 - 8) * 35 = 245 seconds ≈ 4 minutes
```

**Resolution:**

**Increase timeout:**
```bash
uv run tom transcript parse <file> --extractor-timeout 600  # 10 minutes
```

**OR reduce chunk size (re-parse):**
```bash
uv run tom transcript parse <file> --chunk-target-tokens 12000  # Smaller chunks
```

---

#### Issue: Quality Gate Fails Immediately

**Symptom:**
```
ps-critic started
Error: Missing required files - cannot validate
Status: quality_output.status = "failed"
```

**Diagnostic Steps:**

1. **Check packet directory structure:**
```bash
ls -lh /output/transcript-*/
# Should have 00-07 files + _anchors.json
```

2. **Verify ts_formatter_output.files_created:**
```bash
cat /output/.skill-state.json | jq '.ts_formatter_output.files_created'
```

3. **Check for file write errors:**
```bash
cat /output/.skill-state.json | jq '.ts_formatter_output.errors'
```

**Resolution:**

**If files incomplete:**
```bash
# Re-run formatting phase
uv run tom transcript resume --from formatting --packet-path /output/transcript-*/
```

**If permission errors:**
```bash
chmod -R 755 /output/transcript-*/
uv run tom transcript resume --from formatting
```

---

#### Issue: File Conflicts Prevent Execution

**Symptom:**
```
Error: Output directory already exists: /output/transcript-meeting-001/
Conflict detected - refusing to overwrite
```

**Diagnostic Steps:**

1. **Check existing files:**
```bash
ls -lh /output/transcript-meeting-001/
```

2. **Verify if files are from previous run:**
```bash
stat /output/transcript-meeting-001/00-index.md
# Check modification timestamp
```

**Resolution:**

**Option 1: Archive existing output:**
```bash
mv /output/transcript-meeting-001/ /output/archive/transcript-meeting-001-$(date +%Y%m%d-%H%M%S)/
uv run tom transcript parse <file> --output-dir /output/transcript-meeting-001/
```

**Option 2: Use timestamped directory:**
```bash
uv run tom transcript parse <file> --output-dir /output/transcript-meeting-001-$(date +%Y%m%d-%H%M%S)/
```

**Option 3: Merge mode (update only changed files):**
```bash
uv run tom transcript parse <file> --output-dir /output/transcript-meeting-001/ --merge
```

---

#### Issue: Mindmap Generation Partial Failure

**Symptom:**
```
ts-mindmap-mermaid: failed
ts-mindmap-ascii: complete
Status: ts_mindmap_output.overall_status = "partial"
```

**Diagnostic Steps:**

1. **Check Mermaid error message:**
```bash
cat /output/.skill-state.json | jq '.ts_mindmap_output.mermaid.error_message'
```

2. **Verify ASCII mindmap is usable:**
```bash
cat /output/08-mindmap/mindmap.ascii.txt
```

3. **Check if Mermaid file exists (but invalid):**
```bash
ls -lh /output/08-mindmap/mindmap.mmd
head -20 /output/08-mindmap/mindmap.mmd  # Inspect syntax
```

**Resolution:**

**If syntax error (markdown links in nodes):**
```bash
# Regenerate with plain text enforcement
uv run tom transcript mindmap --format mermaid --packet-path /output/ --plain-text-only
```

**If acceptable to use ASCII only:**
```bash
# No action required - ASCII mindmap is valid
cat /output/08-mindmap/mindmap.ascii.txt
```

**If both formats required:**
```bash
# Debug Mermaid generation
uv run tom transcript mindmap --format mermaid --packet-path /output/ --debug
# Fix issues manually, then validate
uv run tom transcript validate-mindmap /output/08-mindmap/mindmap.mmd
```

---

#### Issue: State Key Mismatch (INV-EXT-001 Violation)

**Symptom:**
```
Error: State key mismatch detected
ts_extractor_output.action_count = 23
len(action_items) in extraction-report.json = 25
Violation: INV-EXT-001 (entity count consistency)
ts-formatter refused to proceed
```

**Diagnostic Steps:**

1. **Dump extraction report:**
```bash
cat /output/extraction-report.json | jq '.extraction_stats'
cat /output/extraction-report.json | jq '.action_items | length'
```

2. **Verify state key:**
```bash
cat /output/.skill-state.json | jq '.ts_extractor_output.action_count'
```

3. **Compare values:**
```bash
# Should be exactly equal (tolerance: 0)
```

**Resolution:**

**Option 1: Regenerate extraction report (preferred):**
```bash
rm /output/extraction-report.json
uv run tom transcript resume --from extraction --packet-path /output/
```

**Option 2: Report bug with diagnostic info:**
```bash
uv run tom transcript debug --dump-state /output/ > state-dump.json
# Attach state-dump.json to bug report
# Include extraction-report.json and .skill-state.json
```

**Option 3: Skip validation (CAUTION - may propagate errors):**
```bash
# Only use if deadline-critical and you understand the risk
uv run tom transcript resume --from formatting --skip-validation
```

---

#### Issue: Python Parser Fails, Fallback Doesn't Trigger

**Symptom:**
```
Python VTT parser failed: ModuleNotFoundError: No module named 'webvtt'
Expected: Fallback to LLM parsing
Actual: Pipeline halts with fatal error
```

**Diagnostic Steps:**

1. **Check Python dependencies:**
```bash
uv pip list | grep webvtt
uv pip list | grep tiktoken
```

2. **Verify UV environment:**
```bash
uv sync --verbose
```

3. **Check fallback configuration:**
```bash
cat /output/.skill-state.json | jq '.ts_parser_output.fallback_triggered'
```

**Resolution:**

**Fix dependencies (preferred):**
```bash
uv sync
uv run tom transcript parse <file> --output-dir /output/
```

**Force LLM parsing (bypass Python parser):**
```bash
uv run tom transcript parse <file> --force-llm --output-dir /output/
```

**Manual fallback:**
```bash
# If Python parser consistently fails, use SRT format override
uv run tom transcript parse <file> --format srt --output-dir /output/
# This forces LLM parsing even for VTT files
```

---
