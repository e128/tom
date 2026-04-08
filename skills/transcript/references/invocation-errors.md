# Common Invocation Errors (F-001)

> Extracted from `skills/transcript/SKILL.md` for progressive disclosure (Level 3).
> **Parent:** `skills/transcript/SKILL.md` § Common Invocation Errors

## Document Sections

| Section | Purpose |
|---------|---------|
| [Errors](#error-1-invalid-file-path) | 5 common error patterns with recovery |
| [Input Parameters Reference](#input-parameters-reference) | Full parameter table |

---

## Error 1: Invalid File Path

**What NOT to Do:**
```bash
/transcript meeting.vtt
# Error: File not found - meeting.vtt
```

**Error Output:**
```
Error: Input file 'meeting.vtt' does not exist
Expected: Absolute path or path relative to current working directory
Example: /Users/me/transcripts/meeting.vtt
```

**Correct Invocation:**
```bash
/transcript /Users/me/transcripts/meeting.vtt
# OR with relative path from current directory
/transcript ./transcripts/meeting.vtt
```

---

## Error 2: Unquoted Paths with Spaces

**What NOT to Do:**
```bash
uv run tom transcript parse /Users/me/my meetings/meeting.vtt
# Error: Treats "my" and "meetings/meeting.vtt" as separate arguments
```

**Error Output:**
```
Error: Invalid invocation - multiple positional arguments detected
Detected: ['/Users/me/my', 'meetings/meeting.vtt']
Solution: Quote file paths containing spaces
```

**Correct Invocation:**
```bash
uv run tom transcript parse "/Users/me/my meetings/meeting.vtt"
```

---

## Error 3: Missing Output Directory

**What NOT to Do:**
```bash
/transcript meeting.vtt --output-dir /nonexistent/path/
# Error: Output directory parent does not exist
```

**Error Output:**
```
Error: Cannot create output directory '/nonexistent/path/'
Parent directory '/nonexistent/' does not exist
Solution: Ensure parent directory exists OR use default (./transcript-output/)
```

**Correct Invocation:**
```bash
# Option 1: Use default output directory
/transcript meeting.vtt

# Option 2: Create parent directory first
mkdir -p /path/to/outputs/
/transcript meeting.vtt --output-dir /path/to/outputs/meeting-001/
```

---

## Error 4: Invalid Domain Name

**What NOT to Do:**
```bash
/transcript meeting.vtt --domain engineering
# Error: Domain 'engineering' not recognized
```

**Error Output:**
```
Error: Unknown domain 'engineering'
Available domains: general, transcript, meeting, software-engineering,
  software-architecture, product-management, user-experience,
  cloud-engineering, security-engineering
Did you mean: software-engineering?
```

**Correct Invocation:**
```bash
/transcript meeting.vtt --domain software-engineering
```

---

## Error 5: Conflicting Mindmap Flags

**What NOT to Do:**
```bash
/transcript meeting.vtt --no-mindmap --mindmap-format mermaid
# Error: Contradictory flags
```

**Error Output:**
```
Error: Conflicting flags detected
--no-mindmap: Disables all mindmap generation
--mindmap-format mermaid: Requests specific mindmap format
Solution: Remove one of these flags
```

**Correct Invocation:**
```bash
# Option 1: Disable mindmaps (ignores --mindmap-format)
/transcript meeting.vtt --no-mindmap

# Option 2: Generate Mermaid mindmap only
/transcript meeting.vtt --mindmap-format mermaid
```

## Input Parameters Reference

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `input_file` | string | Yes | - | Path to transcript file |
| `output_dir` | string | No | `./transcript-output/` | Output directory for packet |
| `format` | string | No | auto-detect | Force format: `vtt`, `srt`, `txt` |
| `domain` | string | No | general | Context injection domain (9 available) |
| `confidence_threshold` | float | No | 0.7 | Minimum confidence for extractions |
| `quality_threshold` | float | No | 0.9 | ps-critic quality threshold |
| `--no-mindmap` | flag | No | false | Disable mindmap generation |
| `--mindmap-format` | string | No | "both" | Format: `mermaid`, `ascii`, `both` |
| `--model-parser` | string | No | haiku | Model for ts-parser |
| `--model-extractor` | string | No | sonnet | Model for ts-extractor |
| `--model-formatter` | string | No | sonnet | Model for ts-formatter |
| `--model-mindmap` | string | No | sonnet | Model for ts-mindmap-* |
| `--model-critic` | string | No | sonnet | Model for ps-critic |
