---
name: transcript
description: Parse, extract, and format transcripts (VTT, SRT, plain text) into structured Markdown packets with action items, decisions, questions, and topics. v2.0 uses hybrid Python+LLM architecture for VTT files. Integrates with ps-critic for quality review.
version: "2.5.0"
allowed-tools: Read, Write, Glob, Agent, Bash(*)
argument-hint: <file-path> [--output-dir <dir>] [--no-mindmap] [--mindmap-format <mermaid|ascii|both>]

# CONTEXT INJECTION (implements REQ-CI-F-002)
# Enables domain-specific context loading per SPEC-context-injection.md Section 3.1
# Updated: EN-014 TASK-158 - All 9 domains registered
context_injection:
  # Default domain when none specified
  default_domain: "general"

  # Available domain schemas (9 total)
  # See docs/domains/DOMAIN-SELECTION-GUIDE.md for selection flowchart
  domains:
    # Baseline Domains (3)
    - name: "general"
      description: "Baseline extraction - speakers, topics, questions"
      file: "contexts/general.yaml"
      spec: null  # No specialized spec

    - name: "transcript"
      description: "Base transcript entities - extends general"
      file: "contexts/transcript.yaml"
      spec: null  # No specialized spec

    - name: "meeting"
      description: "Generic meetings - action items, decisions, follow-ups"
      file: "contexts/meeting.yaml"
      spec: null  # No specialized spec

    # Professional Domains (6) - From EN-006 Context Injection Design
    - name: "software-engineering"
      description: "Standups, sprint planning, code reviews - commitments, blockers, risks"
      file: "contexts/software-engineering.yaml"
      spec: "docs/domains/SPEC-software-engineering.md"
      target_users: ["Engineers", "Tech Leads", "Scrum Masters"]

    - name: "software-architecture"
      description: "ADR discussions, design sessions - decisions, alternatives, quality attributes"
      file: "contexts/software-architecture.yaml"
      spec: "docs/domains/SPEC-software-architecture.md"
      target_users: ["Architects", "Principal Engineers"]

    - name: "product-management"
      description: "Roadmap planning, feature prioritization - requests, user needs, stakeholder feedback"
      file: "contexts/product-management.yaml"
      spec: "docs/domains/SPEC-product-management.md"
      target_users: ["PMs", "Product Owners", "Business Analysts"]

    - name: "user-experience"
      description: "Research interviews, usability tests - insights, pain points, verbatim quotes"
      file: "contexts/user-experience.yaml"
      spec: "docs/domains/SPEC-user-experience.md"
      target_users: ["UX Researchers", "UX Designers"]
      special_requirements: ["verbatim_quote_preservation"]

    - name: "cloud-engineering"
      description: "Post-mortems, capacity planning - incidents, root causes, action items"
      file: "contexts/cloud-engineering.yaml"
      spec: "docs/domains/SPEC-cloud-engineering.md"
      target_users: ["SREs", "DevOps Engineers", "Platform Engineers"]
      special_requirements: ["blameless_culture"]

    - name: "security-engineering"
      description: "Security audits, threat modeling - vulnerabilities, threats (STRIDE), compliance gaps"
      file: "contexts/security-engineering.yaml"
      spec: "docs/domains/SPEC-security-engineering.md"
      target_users: ["Security Engineers", "AppSec Engineers", "Compliance Officers"]
      special_requirements: ["risk_acceptance_documentation", "stride_support", "cvss_support"]

  # Context files location
  context_path: "./contexts/"

  # Template variables available to agents
  template_variables:
    - name: domain
      source: invocation.domain
      default: "general"
    - name: entity_definitions
      source: context.entity_definitions
      format: yaml
    - name: extraction_rules
      source: context.extraction_rules
      format: list
    - name: prompt_guidance
      source: context.prompt_guidance
      format: text

activation-keywords:
  - "transcript"
  - "meeting notes"
  - "parse vtt"
  - "parse srt"
  - "extract action items"
  - "extract decisions"
  - "analyze meeting"
  - "/transcript"
---

# MANDATORY: CLI Invocation for Parsing (Phase 1)

> **CRITICAL:** For VTT files, you MUST invoke the Python parser via the `tom` CLI.
> DO NOT use Task agents for parsing. The CLI provides 1,250x cost reduction and deterministic output.

## Phase 1: Parse Transcript (REQUIRED CLI INVOCATION)

**ARGUMENT PARSING RULES:**
1. The FIRST positional argument from user input is the `<file-path>` (the VTT/SRT file)
2. The `--output-dir` flag specifies the output directory (default: `./transcript-output`)
3. **IMPORTANT:** If user provides `--output`, treat it as `--output-dir` (alias)

**For VTT files, Claude MUST execute this bash command:**

```bash
uv run tom transcript parse "<FILE_PATH>" --output-dir "<OUTPUT_DIR>"
```

Where:
- `<FILE_PATH>` = The ACTUAL file path from the user's invocation (first positional arg)
- `<OUTPUT_DIR>` = The output directory from `--output-dir` or `--output` flag (default: `./transcript-output`)

**Example - user invokes:**
```
/transcript /Users/me/meeting.vtt --output-dir /Users/me/output/
```

**Claude executes:**
```bash
uv run tom transcript parse "/Users/me/meeting.vtt" --output-dir "/Users/me/output/"
```

**CRITICAL:** Always quote file paths to handle spaces and special characters.

**Expected output:**
- `index.json` - Chunk metadata and speaker summary
- `chunks/chunk-*.json` - Transcript segments in processable chunks
- `canonical-transcript.json` - Full parsed output (for reference only, DO NOT read into context)

### Tool Example: Invoking the Python Parser

**Claude's execution using Bash tool:**

```bash
# Basic invocation
uv run tom transcript parse "/Users/me/meeting.vtt" --output-dir "/Users/me/output/"
```

**What this does:**
1. Uses `uv run` to execute in managed Python environment
2. Invokes `tom transcript parse` subcommand
3. Quotes paths to handle spaces/special characters
4. Specifies output directory (creates if doesn't exist)

**Common variations:**

```bash
# With domain context
uv run tom transcript parse "meeting.vtt" \
    --output-dir "./output/" \
    --domain software-engineering

# Skip mindmaps for faster processing
uv run tom transcript parse "meeting.vtt" \
    --output-dir "./output/" \
    --no-mindmap

# Specify mindmap format
uv run tom transcript parse "meeting.vtt" \
    --output-dir "./output/" \
    --mindmap-format mermaid
```

**Error handling example:**

```bash
# Check exit code
uv run tom transcript parse "meeting.vtt" --output-dir "./output/"
if [ $? -ne 0 ]; then
    echo "Parsing failed - check error output above"
    exit 1
fi
```

**Verified Output (2026-01-30):**
```
$ uv run tom transcript parse "test.vtt" --output-dir "./out/"
✅ Detected format: VTT
✅ Parsed 3071 segments
✅ Created ./out/index.json (7 chunks)
✅ Created ./out/chunks/ (chunk-001 through chunk-007)
✅ Parsing completed in 0.8s
```

---

## Phase 2+: LLM Agent Orchestration

After Phase 1 CLI parsing completes, continue with LLM agents:
1. **ts-extractor** - Read `index.json` + `chunks/*.json`, produce `extraction-report.json`
2. **ts-formatter** - Read `index.json` + `extraction-report.json`, produce packet files
3. **ts-mindmap-*** - Generate mindmaps (if `--no-mindmap` not set)
4. **ps-critic** - Quality review >= 0.90

---

# Transcript Skill

> **Version:** 2.4.1
> **Framework:** Tom Transcript Processing
> **Constitutional Compliance:** Tom Constitution v1.0 (P-001, P-002, P-003, P-004, P-010, P-020, P-022)
> **Architecture:** Hybrid Python+LLM (Strategy Pattern) + Mindmap Generation + Token-Based Chunking

---

## Document Audience (Triple-Lens)

This SKILL.md serves multiple audiences:

| Level | Audience | Sections to Focus On | Why This Matters |
|-------|----------|---------------------|------------------|
| **L0 (ELI5)** | New users, stakeholders | Purpose, When to Use, [Routing Disambiguation](#routing-disambiguation), Quick Reference | Learn what the skill does and how to invoke it |
| **L1 (Engineer)** | Developers using the skill | Invoking the Skill, Agent Pipeline, File Persistence | Understand the technical workflow and outputs |
| **L2 (Architect)** | Workflow designers | Architecture, State Management, Self-Critique | Design integrations and ensure quality |

**Reading Path Recommendations:**
- **First Time User:** Start with "Purpose" → "When to Use" → "Invoking the Skill" → "Quick Reference"
- **Integration Developer:** Start with "Agent Pipeline" → "State Passing" → "File Persistence"
- **Quality Assurance:** Start with "Self-Critique Protocol" → "Constitutional Compliance" → "Quality Thresholds"

---

## Purpose

The Transcript Skill transforms raw meeting transcripts into structured, navigable knowledge packets. It addresses the **#1 user pain point**: manual extraction of action items, decisions, and key information from meetings.

### Key Capabilities

- **Multi-Format Parsing** - VTT, SRT, and plain text transcript formats
- **Semantic Extraction** - Action items, decisions, questions, topics with confidence scores
- **Speaker Identification** - 4-pattern detection chain for reliable attribution
- **Structured Output** - Claude-optimized Markdown packets under 35K tokens
- **Bidirectional Linking** - Every entity linked to its source in the transcript
- **Quality Review** - Integrated ps-critic evaluation (>= 0.90 threshold)

---

## When to Use This Skill

Activate when:

- Processing a meeting transcript from Zoom, Teams, or other platforms
- Extracting action items and decisions from recorded meetings
- Converting VTT/SRT subtitle files to structured notes
- Analyzing plain text meeting notes
- Generating navigable meeting documentation

**Example Invocations:**
```
"Process this meeting transcript: /path/to/meeting.vtt"
"Extract action items from the quarterly review"
"/transcript analyze-meeting.srt"
"Parse the team standup notes and find all decisions"
"/transcript meeting.vtt --domain software-engineering"
```

---

## Domain Selection

The transcript skill supports **9 domain contexts** that customize entity extraction for specific professional contexts. See [DOMAIN-SELECTION-GUIDE.md](./docs/domains/DOMAIN-SELECTION-GUIDE.md) for the complete selection flowchart.

### Available Domains

| Domain | Context File | Use For | Key Entities |
|--------|--------------|---------|--------------|
| `general` | general.yaml | Any transcript (default) | speakers, topics, questions |
| `transcript` | transcript.yaml | Extends general | + segments, timestamps |
| `meeting` | meeting.yaml | Generic meetings | + action_items, decisions, follow_ups |
| `software-engineering` | software-engineering.yaml | Standups, sprint planning | + commitments, blockers, risks |
| `software-architecture` | software-architecture.yaml | ADR discussions, design | + architectural_decisions, alternatives |
| `product-management` | product-management.yaml | Roadmap, prioritization | + feature_requests, user_needs |
| `user-experience` | user-experience.yaml | Research, usability tests | + user_insights, pain_points, verbatim quotes |
| `cloud-engineering` | cloud-engineering.yaml | Post-mortems, capacity | + incidents, root_causes (blameless) |
| `security-engineering` | security-engineering.yaml | Audits, threat modeling | + vulnerabilities, threats (STRIDE), compliance_gaps |

### Specifying a Domain

```
/transcript <file> --domain <domain-name>
```

**Examples:**
```
/transcript standup.vtt --domain software-engineering
/transcript postmortem.vtt --domain cloud-engineering
/transcript user-interview.vtt --domain user-experience
```

If no domain is specified, `general` is used as the default.

---

## Agent Pipeline

```
TRANSCRIPT SKILL PIPELINE (v2.1 HYBRID ARCHITECTURE + MINDMAPS)
===============================================================

                    USER INPUT (VTT/SRT/TXT)
                           │
                           │ /transcript file.vtt [--mindmap-format both]
                           │ /transcript file.vtt --no-mindmap  (to disable)
                           ▼
    ┌───────────────────────────────────────────────────────┐
    │              ts-parser v2.0 (ORCHESTRATOR)            │
    │          Model: haiku (orchestration only)            │
    └───────────────────────┬───────────────────────────────┘
                            │
           ┌────────────────┴────────────────┐
           │ FORMAT DETECTION                │
           ▼                                 ▼
    ┌─────────────┐                   ┌─────────────┐
    │ VTT Format  │                   │ SRT/TXT     │
    │ (Python)    │                   │ (LLM)       │
    └──────┬──────┘                   └──────┬──────┘
           │                                 │
           ▼                                 │
    ┌─────────────┐                          │
    │  Python VTT │  1,250x cost reduction   │
    │   Parser    │  Sub-second parsing      │
    └──────┬──────┘  100% accuracy           │
           │                                 │
           ▼                                 │
    ┌─────────────┐                          │
    │  VALIDATOR  │                          │
    └──────┬──────┘                          │
           │                                 │
           ▼                                 │
    ┌─────────────┐                          │
    │   Chunker   │                          │
    │  (500 segs) │                          │
    └──────┬──────┘                          │
           │                                 │
           └────────────────┬────────────────┘
                            ▼
    ┌───────────────────────────────────────────────────────┐
    │              ts-extractor (sonnet)                    │
    │          Processes chunks OR monolithic               │
    └───────────────────────┬───────────────────────────────┘
                            │
                            ▼
    ┌───────────────────────────────────────────────────────┐
    │              ts-formatter (sonnet)                    │
    │          Generates 8-file packet per ADR-002          │
    └───────────────────────┬───────────────────────────────┘
                            │
                            │ ts_formatter_output.packet_path
                            ▼
                ┌───────────────────────────┐
                │   --no-mindmap flag set?  │
                └─────────────┬─────────────┘
                              │
           ┌──────────────────┴──────────────────┐
           │ NO (default)                        │ YES
           ▼                                     ▼
    ┌─────────────────────┐              (skip mindmaps)
    │    ts-mindmap-*     │                      │
    │      (sonnet)       │                      │
    │                     │                      │
    │ ┌─────────────────┐ │                      │
    │ │ts-mindmap-mermaid│ │  Output:            │
    │ └─────────────────┘ │  08-mindmap/         │
    │ ┌─────────────────┐ │  mindmap.mmd         │
    │ │ ts-mindmap-ascii│ │  mindmap.ascii.txt   │
    │ └─────────────────┘ │                      │
    └──────────┬──────────┘                      │
               │                                 │
               │ ts_mindmap_output               │
               └──────────────┬──────────────────┘
                              │
                              ▼
    ┌───────────────────────────────────────────────────────┐
    │              ps-critic (sonnet)                       │
    │          Quality validation >= 0.90                   │
    │                                                       │
    │  • Core validation (00-07 files)                      │
    │  • MM-* criteria (if Mermaid mindmap present)         │
    │  • AM-* criteria (if ASCII mindmap present)           │
    └───────────────────────────────────────────────────────┘

COMPLIANCE: Each agent is a WORKER. None spawn subagents.
RATIONALE: DISC-009 - Agent-only architecture caused 99.8% data loss on large files.
MINDMAPS: ADR-006 - Mindmaps ON by default, opt-out via --no-mindmap flag.
```

---

> Design rationale documentation: see [references/design-rationale.md](references/design-rationale.md)

## Available Agents

| Agent | Model | Role | Output |
|-------|-------|------|--------|
| `ts-parser` v2.0 | haiku | **ORCHESTRATOR:** Route VTT→Python, others→LLM. Validate and chunk. | `index.json` + `chunks/*.json` |
| `ts-extractor` | sonnet | Extract speakers, actions, decisions, questions, topics | `extraction-report.json` |
| `ts-formatter` | sonnet | Generate Markdown packet with navigation | `transcript-{id}/` directory |
| `ts-mindmap-mermaid` | sonnet | Generate Mermaid mindmap with deep links (ADR-003) | `08-mindmap/mindmap.mmd` |
| `ts-mindmap-ascii` | sonnet | Generate ASCII art mindmap for terminal display | `08-mindmap/mindmap.ascii.txt` |
| `ps-critic` | sonnet | Validate quality >= 0.90 threshold (includes MM-*/AM-* criteria) | `quality-review.md` |

### Agent Capabilities Summary

**ts-parser v2.0 (Strategy Pattern Orchestrator):**

*Four Roles per TDD-FEAT-004:*
1. **ORCHESTRATOR** - Coordinate pipeline based on format detection
2. **DELEGATOR** - Route VTT to Python parser via Bash tool (1,250x cost reduction)
3. **FALLBACK** - LLM parsing for SRT/TXT formats and error recovery
4. **VALIDATOR** - Verify Python output schema before chunking

*Capabilities:*
- Auto-detect format (VTT header, SRT timestamps, plain text)
- Invoke Python parser for VTT files (deterministic, sub-second)
- Handle encoding detection (UTF-8, Windows-1252, ISO-8859-1)
- Generate chunked output: `index.json` + `chunks/chunk-NNN.json`

**ts-extractor (Research Analyst):**
- 4-pattern speaker detection chain (PAT-003)
- Tiered extraction: Rule → ML → LLM (PAT-001)
- Confidence scoring (0.0-1.0) for all entities
- Mandatory citations for every extraction (PAT-004)

**ts-formatter (Publishing House):**
- ADR-002 packet structure (8 files)
- ADR-004 file splitting at semantic boundaries (31.5K soft limit)
- ADR-003 anchor registry and bidirectional backlinks
- Token counting and limit enforcement

**ts-mindmap-mermaid (Visualization - Mermaid):**
- Generates Mermaid mindmap syntax from extraction report
- Topic hierarchy with entity grouping
- Deep links to transcript anchors (ADR-003 format)
- Entity symbols: → (action), ? (question), ! (decision), ✓ (follow-up)
- Maximum 50 topics (overflow handling)

**ts-mindmap-ascii (Visualization - ASCII):**
- Generates ASCII art mindmap for terminal display
- UTF-8 box-drawing characters for tree structure
- 80-character line width limit
- Legend at bottom explaining entity symbols
- Terminal-friendly fallback when Mermaid rendering unavailable

**ps-critic (Quality Inspector):**
- Quality score calculation (aggregate >= 0.90)
- Requirements traceability verification
- ADR compliance checking
- Improvement recommendations
- MM-* criteria validation (if Mermaid mindmap present)
- AM-* criteria validation (if ASCII mindmap present)

### Tool Example: Invoking Agents via Task Tool

**Orchestrator invokes ts-extractor:**

```
Invoke Task tool with:
- agent: "ts-extractor"
- task: "Extract entities from chunked transcript"
- inputs:
    - index_json_path: "<output-dir>/index.json"
    - chunks_dir: "<output-dir>/chunks/"
    - confidence_threshold: 0.7
    - domain: "software-engineering"
```

**ts-extractor's internal workflow:**

1. Read index.json (metadata)
2. For each chunk reference:
   - Read chunk file
   - Extract speakers, actions, decisions, questions, topics
   - Assign confidence scores
   - Add source citations
3. Aggregate results into extraction-report.json
4. Write extraction-report.json
5. Return extraction_report_path in state

**Orchestrator invokes ts-mindmap-mermaid (conditional):**

```
IF --no-mindmap flag NOT set:  # Default behavior
    Invoke Task tool with:
    - agent: "ts-mindmap-mermaid"
    - task: "Generate Mermaid mindmap from extraction report"
    - inputs:
        - extraction_report_path: "<output-dir>/extraction-report.json"
        - packet_path: "<packet-dir>/"
        - max_topics: 50
```

**Orchestrator invokes ps-critic:**

```
Invoke Task tool with:
- agent: "ps-critic"
- task: "Validate transcript packet quality"
- inputs:
    - packet_path: "<packet-dir>/"
    - mindmap_path: "<packet-dir>/08-mindmap/"  # If present
    - quality_threshold: 0.90
    - extension_file: "skills/transcript/validation/ts-critic-extension.md"
```

**Agent invocation sequencing:**

```
SEQUENTIAL (cannot parallelize due to dependencies):
1. ts-parser → outputs index.json + chunks/
2. ts-extractor → reads index.json, outputs extraction-report.json
3. ts-formatter → reads index.json + extraction-report.json, outputs packet/
4. ts-mindmap-* → reads extraction-report.json + packet/, outputs 08-mindmap/
5. ps-critic → reads packet/ + 08-mindmap/, outputs quality-review.md
```

---

## Invoking the Skill

> **CRITICAL:** The transcript skill execution follows a multi-phase workflow. Phase 1 MUST be executed via the tom CLI. Subsequent phases use LLM agents.

### Natural Language Trigger Patterns

The transcript skill responds to these natural language patterns:

| Pattern Type | Examples | Detected As |
|--------------|----------|-------------|
| **Direct file reference** | "Process meeting.vtt"<br>"Parse the transcript at /path/to/file" | File path extraction |
| **Action-oriented** | "Extract action items from..."<br>"Analyze the team meeting..." | Task + implicit file |
| **Domain-specific** | "Generate mindmap from standup"<br>"Process the architecture review" | Feature + implicit file |
| **Slash command** | `/transcript meeting.vtt`<br>`/transcript parse file.srt` | Explicit skill invocation |

**Skill Activation Keywords** (from header):
- "transcript"
- "meeting notes"
- "parse vtt" / "parse srt"
- "extract action items" / "extract decisions"
- "analyze meeting"
- "/transcript"

### Option 1: Slash Command (Explicit)

```bash
/transcript <file-path> [OPTIONS]
```

**Available Options:**
```
--output-dir <dir>              # Output directory (default: ./transcript-output/)
--format <vtt|srt|txt>          # Force format detection
--domain <domain-name>          # Context injection domain (default: general)
--no-mindmap                    # Disable mindmap generation (mindmaps ON by default)
--mindmap-format <format>       # mermaid | ascii | both (default: both)
--model-parser <model>          # haiku | sonnet | opus (default: haiku)
--model-extractor <model>       # haiku | sonnet | opus (default: sonnet)
--model-formatter <model>       # haiku | sonnet | opus (default: sonnet)
--model-mindmap <model>         # haiku | sonnet | opus (default: sonnet)
--model-critic <model>          # haiku | sonnet | opus (default: sonnet)
```

**Examples (Basic Usage - Default Mindmaps):**
```bash
/transcript meeting.vtt                                   # Mindmaps ON (both formats)
/transcript standup.srt --output-dir ./docs/meetings/     # With output directory
/transcript notes.txt --format txt                        # Force format detection
/transcript meeting.vtt --domain software-engineering     # With domain context
```

**Examples (Mindmap Control):**
```bash
/transcript meeting.vtt --mindmap-format mermaid          # Only Mermaid format
/transcript meeting.vtt --mindmap-format ascii            # Only ASCII format
/transcript meeting.vtt --mindmap-format both             # Both formats (explicit)
/transcript meeting.vtt --no-mindmap                      # Skip mindmap generation
```

**Examples (Model Selection):**
```bash
# Higher quality extraction (use Opus for entities)
/transcript meeting.vtt --model-extractor opus

# Lower cost processing (use Haiku for all agents)
/transcript meeting.vtt \
    --model-parser haiku \
    --model-extractor haiku \
    --model-formatter haiku \
    --model-mindmap haiku \
    --model-critic haiku

# Balanced optimization (Haiku for templates, Sonnet for semantic work)
/transcript meeting.vtt \
    --model-parser haiku \
    --model-formatter haiku \
    --model-mindmap haiku
```

### Option 2: Natural Language (Implicit)

```
"Process the transcript at /path/to/meeting.vtt"
"Extract action items from yesterday's team meeting"
"Analyze the quarterly review transcript and create a summary"
"Process the meeting transcript and generate mindmaps"
"Parse the standup notes without mindmaps"
"Create a Mermaid-only mindmap from the transcript"
"Use high-quality extraction for this transcript" (triggers --model-extractor opus)
```

**Detection Algorithm:**
Parse the user's message for the transcript file path, output directory, and implied options (e.g., "without mindmaps" → `--no-mindmap`, "high quality" → `--model-extractor opus`, domain context → `--domain`), then construct and execute the equivalent `uv run tom transcript parse` invocation.

---

## Common Invocation Errors (F-001)

> **PURPOSE:** Learn from common mistakes to avoid failed invocations and understand error recovery.

### Error 1: Invalid File Path

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

### Error 2: Unquoted Paths with Spaces

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

### Error 3: Missing Output Directory

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

### Error 4: Invalid Domain Name

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

### Error 5: Conflicting Mindmap Flags

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

### Input Parameters Reference

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

---

## Model Selection

The transcript skill supports configurable models for each agent to optimize cost and quality.

### Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--model-parser` | haiku | Model for ts-parser (orchestration, routing) |
| `--model-extractor` | sonnet | Model for ts-extractor (entity extraction) |
| `--model-formatter` | sonnet | Model for ts-formatter (packet generation) |
| `--model-mindmap` | sonnet | Model for ts-mindmap-* (visualization) |
| `--model-critic` | sonnet | Model for ps-critic (quality review) |

**Valid Model Values:** `haiku`, `sonnet`, `opus`

### Cost Optimization

Based on Anthropic Claude pricing (as of 2026-01-30) for 10,000 input tokens:

| Configuration | Estimated Cost | Quality Trade-off | Use Case |
|---------------|----------------|-------------------|----------|
| **Default (mixed)** | ~$0.12 | Balanced cost and quality | Recommended for most workflows |
| **All haiku** | ~$0.015 | 88% savings, lower extraction quality | Budget-constrained, simple transcripts |
| **All sonnet** | ~$0.15 | Baseline quality | Consistent quality across all agents |
| **All opus** | ~$0.75 | Highest quality, 6x cost | Critical meetings, high-stakes content |

**Cost Breakdown (Default):**
- ts-parser (haiku): ~$0.0025 - Simple orchestration
- ts-extractor (sonnet): ~$0.06 - Most token-intensive agent
- ts-formatter (sonnet): ~$0.03 - Template-based generation
- ts-mindmap-* (sonnet): ~$0.015 - Hierarchical reasoning
- ps-critic (sonnet): ~$0.015 - Quality evaluation

### Usage Examples

#### Economy Mode (Minimize Cost)

```bash
# Use haiku for all agents except extractor
uv run tom transcript parse meeting.vtt \
    --model-parser haiku \
    --model-extractor haiku \
    --model-formatter haiku \
    --model-mindmap haiku \
    --model-critic haiku

# Cost: ~$0.015 per 10K tokens
# Trade-off: Lower entity extraction accuracy (~70-75%)
```

#### Quality Mode (Maximum Accuracy)

```bash
# Use opus for critical extraction and review
uv run tom transcript parse meeting.vtt \
    --model-extractor opus \
    --model-critic opus

# Cost: ~$0.45 per 10K tokens (with default haiku/sonnet mix)
# Trade-off: 3.75x cost increase, highest extraction accuracy (~95%+)
```

#### Balanced Mode (Default)

```bash
# Use defaults (mixed haiku/sonnet)
uv run tom transcript parse meeting.vtt

# Cost: ~$0.12 per 10K tokens
# Trade-off: Optimal cost/quality balance (~85-90% accuracy)
```

#### Custom Mix (Targeted Optimization)

```bash
# Use haiku for formatting (template-based, low semantic complexity)
# Keep sonnet for extraction and review (semantic understanding required)
uv run tom transcript parse meeting.vtt \
    --model-formatter haiku \
    --model-mindmap haiku

# Cost: ~$0.09 per 10K tokens
# Trade-off: 25% savings with minimal quality impact
```

### Recommendations

| Agent | Recommended Model | Rationale |
|-------|------------------|-----------|
| **ts-parser** | haiku | Minimal semantic work - orchestration and routing only |
| **ts-extractor** | sonnet or opus | Core extraction quality - most critical for accuracy |
| **ts-formatter** | haiku or sonnet | Template-based generation - haiku sufficient if extraction is good |
| **ts-mindmap-*** | sonnet | Hierarchical reasoning - benefits from sonnet's structure understanding |
| **ps-critic** | sonnet | Quality evaluation - needs reliable judgment |

**When to Upgrade to Opus:**
- Legal, medical, or financial transcripts (high-stakes content)
- Poor automatic transcription quality (many errors)

---

## Model Profiles

Model profiles provide quick-select configurations optimized for common use cases. Profiles replace manual configuration of individual `--model-*` flags.

### Available Profiles

| Profile | Description | Use Case | Trade-off |
|---------|-------------|----------|-----------|
| **economy** | All haiku | High-volume processing, budget constraints | Lower extraction quality (~70-75% accuracy) |
| **balanced** | Mixed haiku/sonnet (default) | General purpose processing | Balanced cost and quality (~85-90% accuracy) |
| **quality** | Opus for critical agents | Critical meetings, complex content | Higher cost (~3.75x increase) |
| **speed** | All haiku | Real-time processing, quick turnaround | Quality for speed (~70-75% accuracy) |

### Profile Model Assignments

| Agent | economy | balanced | quality | speed |
|-------|---------|----------|---------|-------|
| ts-parser | haiku | haiku | sonnet | haiku |
| ts-extractor | haiku | sonnet | **opus** | haiku |
| ts-formatter | haiku | haiku | sonnet | haiku |
| ts-mindmap-* | haiku | sonnet | sonnet | haiku |
| ps-critic | haiku | sonnet | **opus** | haiku |

### Usage

#### Select a Profile

```bash
# Use economy profile (all haiku)
uv run tom transcript parse meeting.vtt --profile economy

# Use quality profile (opus for extractor and critic)
uv run tom transcript parse meeting.vtt --profile quality

# Use speed profile (same as economy, but emphasizes latency)
uv run tom transcript parse meeting.vtt --profile speed
```

#### Override Individual Models

Individual `--model-*` flags take precedence over `--profile`:

```bash
# Use economy profile, but upgrade extractor to opus
uv run tom transcript parse meeting.vtt \
    --profile economy \
    --model-extractor opus

# Result: haiku for all agents EXCEPT extractor (opus)
```

```bash
# Use quality profile, but downgrade formatter to haiku
uv run tom transcript parse meeting.vtt \
    --profile quality \
    --model-formatter haiku

# Result: opus for extractor/critic, sonnet for parser/mindmap, haiku for formatter
```

### Default Behavior

If neither `--profile` nor individual `--model-*` flags are specified:
- **Default profile:** `balanced`
- **Equivalent to:** `--profile balanced`

### Priority Resolution

Model selection follows this precedence (highest to lowest):

1. **Explicit `--model-*` flags** (highest priority)
2. **`--profile` flag**
3. **Default profile** (`balanced`)

**Example:**

```bash
# What model does ts-extractor use?
uv run tom transcript parse meeting.vtt
# → sonnet (from default "balanced" profile)

uv run tom transcript parse meeting.vtt --profile economy
# → haiku (from "economy" profile)

uv run tom transcript parse meeting.vtt --profile economy --model-extractor opus
# → opus (explicit flag overrides profile)
```

### Cost Comparison

Based on 10,000 input tokens:

| Profile | Estimated Cost | vs. Balanced |
|---------|----------------|--------------|
| economy | ~$0.015 | **88% savings** |
| balanced (default) | ~$0.12 | Baseline |
| quality | ~$0.45 | 3.75x increase |
| speed | ~$0.015 | **88% savings** |

### When to Use Each Profile

**economy:**
- High-volume batch processing
- Budget constraints
- Simple transcripts with minimal context
- Non-critical content

**balanced (default):**
- General purpose processing
- Most workflows
- Good cost/quality trade-off
- Recommended starting point

**quality:**
- Critical meetings (executive, legal, medical)
- Complex technical discussions
- Poor transcription quality (many errors)
- High-stakes content requiring accuracy

**speed:**
- Real-time processing needs
- Quick turnaround requirements
- Low-latency workflows
- Same cost as economy, emphasizes speed over quality
- Complex domain-specific terminology
- Critical meetings requiring maximum accuracy

**When to Use Haiku:**
- Simple, well-structured transcripts
- Budget constraints
- Low-stakes internal meetings
- Good automatic transcription quality

---

## Output Structure (ADR-002 + v2.0 Hybrid)

```
transcript-{id}/
├── canonical/                  # v2.0: Hybrid parser output
│   ├── canonical-transcript.json  # Full parsed transcript
│   ├── index.json              # Chunk index with metadata
│   └── chunks/                 # Chunked segments (500 per file)
│       ├── chunk-000.json      # Segments 0-499
│       ├── chunk-001.json      # Segments 500-999
│       └── ...
├── 00-index.md                 # Navigation hub (~2K tokens)
├── 01-summary.md               # Executive summary (~5K tokens)
├── 02-transcript.md            # Full transcript (may split)
├── 03-speakers.md              # Speaker directory
├── 04-action-items.md          # Action items with citations
├── 05-decisions.md             # Decisions with context
├── 06-questions.md             # Open questions
├── 07-topics.md                # Topic segments
├── 08-mindmap/                 # Mindmap directory (default: enabled, per ADR-006)
│   ├── mindmap.mmd             # Mermaid format (if --mindmap-format mermaid or both)
│   └── mindmap.ascii.txt       # ASCII format (if --mindmap-format ascii or both)
└── _anchors.json               # Anchor registry for linking
```

### v2.0 Chunked Structure (index.json)

```json
{
  "schema_version": "1.0",
  "generated_at": "2026-01-30T18:00:00Z",
  "total_segments": 710,
  "total_chunks": 4,
  "chunk_size": 500,
  "target_tokens": 18000,
  "duration_ms": 2263888,
  "speakers": {
    "count": 3,
    "list": ["Alex Johnson", "Sam Chen", "Jordan Lee"],
    "segment_counts": {"Alex Johnson": 459, "Sam Chen": 156, "Jordan Lee": 95}
  },
  "chunks": [
    {
      "chunk_id": "chunk-001",
      "segment_range": [1, 229],
      "timestamp_range": {"start_ms": 3528, "end_ms": 721925},
      "speaker_counts": {"Alex Johnson": 151, "Sam Chen": 39, "Jordan Lee": 39},
      "word_count": 2193,
      "file": "chunks/chunk-001.json"
    }
  ]
}
```

**Key Fields:**
- `target_tokens`: When set (e.g., 18000), uses token-based chunking. When `null`, uses segment-based (500 segs/chunk).
- `chunk_size`: Fallback for segment-based mode (used when `target_tokens` is null).
- See DISC-001 for ~22% JSON serialization overhead (18K target → ~22K actual).

### Chunk Token Budget (v2.1 - EN-026)

| Parameter | Value | Source |
|-----------|-------|--------|
| Claude Code Read limit | 25,000 tokens | GitHub Issue #4002 |
| Target tokens per chunk | 18,000 tokens | 25% safety margin |
| Token counting | tiktoken p50k_base | Best Claude approximation |

**Note:** Prior to v2.1, chunks used segment-based splitting (500 segments per chunk).
v2.1 uses **token-based splitting** to ensure chunks fit within Claude Code's Read tool limits.
This fixes BUG-001 where large transcripts produced chunks exceeding the 25K token limit.

### Token Budget Compliance (ADR-004)

| Limit | Tokens | Action |
|-------|--------|--------|
| Soft | 31,500 | Split at ## heading |
| Hard | 35,000 | Force split |

### Model-Agnostic Output Requirements (ADR-007)

> **CRITICAL:** Output structure MUST be identical regardless of which LLM model (Sonnet, Opus, Haiku) executes the skill. ADR-007 defines the golden template specification.

#### MUST-CREATE Files (Exactly 8 Core Files)

| Number | File | Description |
|--------|------|-------------|
| 00 | `00-index.md` | Navigation hub and metadata |
| 01 | `01-summary.md` | Executive summary |
| 02 | `02-transcript.md` | Full formatted transcript (splittable) |
| 03 | `03-speakers.md` | Speaker directory |
| 04 | `04-action-items.md` | Action items with citations |
| 05 | `05-decisions.md` | Decisions with context |
| 06 | `06-questions.md` | Open and answered questions |
| 07 | `07-topics.md` | Topic hierarchy |

**Also Required:** `_anchors.json` (anchor registry)

#### MUST-NOT-CREATE Files (Validation Failure)

| Forbidden Pattern | Reason |
|-------------------|--------|
| `*-timeline.md` | Not part of ADR-002 schema |
| `*-sentiment.md` | Not part of ADR-002 schema |
| `*-analysis.md` | Not part of ADR-002 schema |
| `08-*.md` | 08 reserved for mindmap directory |
| Unnumbered `*.md` | All core files must be numbered 00-07 |

#### Anchor Format (MUST USE)

| Entity | Pattern | Valid | Invalid |
|--------|---------|-------|---------|
| Segment | `seg-NNN` | seg-001 | segment-001, SEG-001 |
| Speaker | `spk-{slug}` | spk-alice-smith | speaker-alice |
| Action | `act-NNN` | act-001 | AI-001, ACT-001 |
| Decision | `dec-NNN` | dec-001 | DEC-001 |
| Question | `que-NNN` | que-001 | QUE-001 |
| Topic | `top-NNN` | top-001 | TOP-001 |

**NNN = 3-digit, zero-padded (001-999)**

#### Citation Format (MUST USE)

```markdown
> "{QUOTED_TEXT}"
>
> -- [{SPEAKER}](03-speakers.md#{spk-slug}), [[{TIMESTAMP}]](02-transcript.md#{seg-NNN})
```

**FORBIDDEN:** Links to `canonical-transcript.json` (file too large for LLM context)

#### Navigation Links (MUST INCLUDE)

Every entity file (01-07) MUST include:

```markdown
## Navigation

- [Back to Index](00-index.md)
- [Previous: {PREV_FILE_NAME}]({PREV_FILE}.md)
- [Next: {NEXT_FILE_NAME}]({NEXT_FILE}.md)
```

**Reference:** See [ADR-007](../../projects/PROJ-008-transcript-skill/work/EPIC-001-transcript-skill/FEAT-006-output-consistency/docs/decisions/ADR-007-output-template-specification.md) for complete specification.

### Tool Example: Writing Packet Files

**ts-formatter generates packet files using Write tool:**

```
# Create 00-index.md
Invoke Write tool with:
- file_path: "<packet-dir>/00-index.md"
- content: (generated index content with navigation links)

# Create 01-summary.md
Invoke Write tool with:
- file_path: "<packet-dir>/01-summary.md"
- content: (executive summary with key findings)

# Create 04-action-items.md
Invoke Write tool with:
- file_path: "<packet-dir>/04-action-items.md"
- content: (action items with citations and anchors)
```

**Content structure example (04-action-items.md):**

```markdown
# Action Items

<!-- Anchor: #act-001 -->
## 1. Implement user authentication

**Assigned to:** Alice
**Priority:** High
**Due date:** Next sprint

**Source:**
- Timestamp: [00:15:32]
- Speaker: Alice (#spk-001)
- Utterance: #utt-042

**Context:**
> "We need to implement user authentication before the beta launch. I'll take this on for next sprint."

---

<!-- Anchor: #act-002 -->
## 2. Fix navigation bug

...
```

**File size validation:**

```
After writing each file:
    Count tokens using Claude's tokenizer
    IF tokens > 35000:
        Split at semantic boundary (## heading)
        Create part-002, part-003, etc.
```

---

## Agent File Consumption Rules (CRITICAL)

> **MANDATORY:** Agents MUST follow these file consumption rules to prevent context window overflow.
> Violating these rules causes degraded performance and potential failures.

### Files Agents SHOULD Read

| File | Typical Size | Agent | Purpose |
|------|--------------|-------|---------|
| `index.json` | ~8KB | ts-extractor, ts-formatter | Metadata, speaker list, chunk references |
| `chunks/chunk-*.json` | ~130KB each | ts-extractor | Actual transcript data in manageable pieces |
| `extraction-report.json` | ~35KB | ts-formatter, ps-critic | Entity extraction results |
| `packet/*.md` | Variable | ps-critic | Generated Markdown files for quality review |

### Files Agents MUST NEVER Read

| File | Typical Size | Why Forbidden |
|------|--------------|---------------|
| `canonical-transcript.json` | **~930KB** | **TOO LARGE** - will overwhelm context window, cause context rot, degrade agent performance |

### Rationale

The `canonical-transcript.json` file is generated for:
- **Reference/archive purposes** - Human inspection of full parsed output
- **Programmatic access by Python code** - CLI tools that process outside LLM context
- **NOT for LLM agent consumption** - File size exceeds safe context limits

The chunking architecture (DISC-009) was specifically designed to solve the large file problem:
- Each chunk is < 150KB (fits comfortably in context)
- Python parser creates chunks; LLM agents consume chunks
- This prevents the 99.8% data loss experienced with agent-only architecture

### Agent-Specific File Access

| Agent | Reads | Never Reads |
|-------|-------|-------------|
| **ts-parser** | Input VTT/SRT/TXT file | - |
| **ts-extractor** | `index.json`, `chunks/*.json` | `canonical-transcript.json` |
| **ts-formatter** | `index.json`, `extraction-report.json` | `canonical-transcript.json` |
| **ps-critic** | All `packet/*.md` files, `quality-review.md` | `canonical-transcript.json` |

---

## Orchestration Flow

### L1: Step-by-Step Pipeline (v2.0 Hybrid)

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

### L2: State Passing Between Agents (v2.0)

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

**State Schema (v2.0):**
```yaml
ts_parser_output:
  # === Core Parsing Results (v2.0 Chunked Architecture) ===
  canonical_json_path: string          # Full transcript JSON (archive only, ~930KB)
  index_json_path: string              # Chunk index metadata (~8KB)
  chunks_dir: string                   # chunks/ directory path
  chunk_count: integer                 # Number of chunk files created

  # === Parsing Metadata ===
  format_detected: vtt|srt|plain       # Auto-detected or forced format
  parsing_method: python|llm           # Strategy Pattern routing decision
  segment_count: integer               # Total segments in transcript
  speaker_count: integer               # Unique speakers identified
  duration_ms: integer|null            # Transcript duration (null for plain text)

  # === Quality/Validation ===
  validation_passed: boolean           # Schema validation result
  warnings: string[]                   # Non-fatal parsing issues

  # === Error Handling ===
  errors: string[]                     # Fatal errors (if any)
  fallback_triggered: boolean          # True if Python→LLM fallback occurred

ts_extractor_output:
  # === Core Extraction Results ===
  extraction_report_path: string       # Path to extraction-report.json (~35KB)

  # === Entity Counts (MUST match array lengths per INV-EXT-001) ===
  action_count: integer                # len(action_items) - MANDATORY consistency
  decision_count: integer              # len(decisions) - MANDATORY consistency
  question_count: integer              # len(questions) - MANDATORY consistency
  topic_count: integer                 # len(topics) - MANDATORY consistency
  speaker_count: integer               # len(speakers) - MANDATORY consistency

  # === Quality Metrics ===
  high_confidence_ratio: float         # Ratio of high-confidence extractions
  average_confidence: float            # Mean confidence across all entities

  # === Processing Metadata ===
  chunks_processed: integer            # Number of chunks analyzed
  input_format: "chunked"|"single_file" # Input format used

  # === Tiered Extraction Stats ===
  tier_1_count: integer                # Rule-based extractions (high confidence)
  tier_2_count: integer                # ML-based extractions (medium confidence)
  tier_3_count: integer                # LLM-based extractions (variable confidence)

ts_formatter_output:
  # === Core Output ===
  packet_path: string                  # Directory path to 8-file packet

  # === File Manifest ===
  files_created: string[]              # List of all created files
  split_files: integer                 # Number of files split due to token limits

  # === Token Accounting ===
  total_tokens: integer                # Sum of tokens across all files
  max_file_tokens: integer             # Largest file token count

  # === Linking Metadata ===
  anchor_count: integer                # Total anchors in registry
  backlink_count: integer              # Total backlinks generated

  # === Validation ===
  all_files_under_limit: boolean       # True if all < 35K tokens per ADR-004

ts_mindmap_output:                      # NEW: ADR-006 State Passing (see ADR-006#state-passing)
  # === Mindmap Control ===
  enabled: boolean                      # Was --no-mindmap NOT set?
  format_requested: string              # "mermaid" | "ascii" | "both"

  # === Mermaid Mindmap ===
  mermaid:
    path: string | null                 # Path to 08-mindmap/mindmap.mmd
    status: string                      # "complete" | "failed" | "skipped"
    error_message: string | null        # Error if status="failed"
    topic_count: integer                # Topics included in mindmap
    deep_link_count: integer            # Deep links in reference block
    syntax_validated: boolean           # Mermaid syntax check passed

  # === ASCII Mindmap ===
  ascii:
    path: string | null                 # Path to 08-mindmap/mindmap.ascii.txt
    status: string                      # "complete" | "failed" | "skipped"
    error_message: string | null        # Error if status="failed"
    topic_count: integer                # Topics included in mindmap
    max_line_width: integer             # Maximum line width used (should be <= 80)
    box_drawing_valid: boolean          # UTF-8 box-drawing characters validated

  # === Overall Status ===
  overall_status: string                # "complete" | "partial" | "failed" | "skipped"
  regeneration_command: string | null   # Command to regenerate if failed

quality_output:
  # === Quality Score ===
  quality_score: float                  # Aggregate score (0.0-1.0)
  passed: boolean                       # True if >= quality_threshold (default 0.90)

  # === Validation Results ===
  issues: string[]                      # Quality gate failures
  recommendations: string[]             # Improvement suggestions

  # === Criteria Breakdown ===
  criteria_scores: dict                 # Per-criterion scores (e.g., "T-001": 0.95)
  mindmap_criteria_applied: boolean     # True if MM-*/AM-* criteria checked

  # === Traceability ===
  artifacts_validated: string[]         # List of files checked
  validation_timestamp: string          # ISO 8601 timestamp
```

---

> Error state structures and recovery documentation: see [references/error-handling.md](references/error-handling.md)

## Error Handling

| Error | Detection | Recovery |
|-------|-----------|----------|
| File not found | OS exception | Return clear error message |
| Unknown format | Auto-detect fails | Fallback to plain text parser |
| Encoding error | Decode exception | Try UTF-8, Windows-1252, ISO-8859-1 |
| Token overflow | Count > soft limit | Split at semantic boundary |
| Low confidence | score < threshold | Include in "uncertain" section |
| Quality failure | score < 0.90 | Report issues for human review |

---

## File Persistence Requirements (P-002 Compliance)

> **CRITICAL:** All transcript skill outputs MUST be persisted to the filesystem.
> Violating P-002 (File Persistence) is a constitutional violation.

### Mandatory Artifacts by Agent

**ts-parser v2.0:**
| Artifact | Path | Size | Purpose | Required |
|----------|------|------|---------|----------|
| Canonical JSON | `canonical-transcript.json` | ~930KB | Archive, programmatic access | ✓ Yes |
| Index JSON | `index.json` | ~8KB | Chunk metadata, agent input | ✓ Yes |
| Chunk Files | `chunks/chunk-NNN.json` | ~130KB each | LLM-processable segments | ✓ Yes |

**ts-extractor:**
| Artifact | Path | Size | Purpose | Required |
|----------|------|------|---------|----------|
| Extraction Report | `extraction-report.json` | ~35KB | Entity extraction results | ✓ Yes |

**ts-formatter:**
| Artifact | Path | Size | Purpose | Required |
|----------|------|------|---------|----------|
| 00-index.md | `packet/00-index.md` | ~2KB | Navigation hub | ✓ Yes |
| 01-summary.md | `packet/01-summary.md` | ~5KB | Executive summary | ✓ Yes |
| 02-transcript.md | `packet/02-transcript.md` | Variable | Full transcript (may split) | ✓ Yes |
| 03-speakers.md | `packet/03-speakers.md` | ~3KB | Speaker directory | ✓ Yes |
| 04-action-items.md | `packet/04-action-items.md` | ~4KB | Action items with citations | ✓ Yes |
| 05-decisions.md | `packet/05-decisions.md` | ~3KB | Decisions with context | ✓ Yes |
| 06-questions.md | `packet/06-questions.md` | ~2KB | Open questions | ✓ Yes |
| 07-topics.md | `packet/07-topics.md` | ~3KB | Topic segments | ✓ Yes |
| _anchors.json | `packet/_anchors.json` | ~5KB | Anchor registry for linking | ✓ Yes |

**ts-mindmap-mermaid (conditional):**
| Artifact | Path | Size | Purpose | Required |
|----------|------|------|---------|----------|
| Mermaid Mindmap | `packet/08-mindmap/mindmap.mmd` | ~10KB | Mermaid visualization | If `--mindmap-format=mermaid` or `both` |

**ts-mindmap-ascii (conditional):**
| Artifact | Path | Size | Purpose | Required |
|----------|------|------|---------|----------|
| ASCII Mindmap | `packet/08-mindmap/mindmap.ascii.txt` | ~8KB | Terminal-friendly visualization | If `--mindmap-format=ascii` or `both` |

**ps-critic:**
| Artifact | Path | Size | Purpose | Required |
|----------|------|------|---------|----------|
| Quality Review | `packet/quality-review.md` | ~15KB | Quality validation results | ✓ Yes |

### Agent File Persistence Checklist

**Before completing execution, EACH agent MUST:**

```yaml
ts-parser:
  - [ ] Write canonical-transcript.json to disk
  - [ ] Write index.json to disk
  - [ ] Create chunks/ directory
  - [ ] Write all chunk-NNN.json files
  - [ ] Verify all files exist and are readable
  - [ ] Report file paths in ts_parser_output state

ts-extractor:
  - [ ] Write extraction-report.json to disk
  - [ ] Verify file exists and is valid JSON
  - [ ] Verify entity counts match array lengths (INV-EXT-001)
  - [ ] Report file path in ts_extractor_output state

ts-formatter:
  - [ ] Create packet directory (mkdir -p)
  - [ ] Write ALL 8 core files (00-index.md through 07-topics.md)
  - [ ] Write _anchors.json
  - [ ] Create split files if any file exceeds soft limit (31.5K tokens)
  - [ ] Verify all files exist
  - [ ] Verify all files are under hard limit (35K tokens per ADR-004)
  - [ ] Report file list in ts_formatter_output.files_created

ts-mindmap-mermaid:
  - [ ] Create 08-mindmap/ directory (if not exists)
  - [ ] Write mindmap.mmd file
  - [ ] Verify Mermaid syntax is valid
  - [ ] Verify deep link reference block is present
  - [ ] Report file path in ts_mindmap_output.mermaid.path

ts-mindmap-ascii:
  - [ ] Ensure 08-mindmap/ directory exists
  - [ ] Write mindmap.ascii.txt file
  - [ ] Verify all lines are <= 80 characters
  - [ ] Verify legend is present
  - [ ] Report file path in ts_mindmap_output.ascii.path

ps-critic:
  - [ ] Write quality-review.md to packet directory
  - [ ] Include all validation criteria results
  - [ ] List issues and recommendations
  - [ ] Report quality score in quality_output state
```

### Persistence Failure Recovery

**If an agent fails to persist:**

1. **Detection:** Post-completion check fails (file_must_exist validation)
2. **Response:** Agent returns error status, pipeline halts
3. **Recovery:** Fix the persistence issue, retry agent execution
4. **Never:** Proceed to next agent without verifying file existence

---

> Agent self-critique protocol documentation: see [references/self-critique-protocol.md](references/self-critique-protocol.md)

---

## Constitutional Compliance

| Principle | Requirement | Consequence of Violation |
|-----------|-------------|-------------------------|
| P-003 | NEVER spawn recursive subagents -- max 1 level | Agent hierarchy violation; uncontrolled token consumption |
| P-020 | NEVER override user intent -- ask before destructive ops | Unauthorized action; trust erosion |
| P-022 | NEVER deceive about actions, capabilities, or confidence | Governance undermined; quality assessment invalidated |
| P-001 | NEVER present findings without evidence -- self-critique protocol enforced | Unreliable outputs; unfounded claims propagate downstream |
| P-002 | NEVER leave outputs in transient context only -- persist all outputs to files | Context rot vulnerability; artifacts lost on session compaction |
| P-004 | NEVER omit citations or provenance -- all extractions require deep links | Untraceable decisions; audit trail broken |
| P-010 | NEVER misrepresent task state -- state outputs must match actual results | Work progress invisible; status unknown |

---

## Quick Reference

> **ELI5 (Level 0):** This section provides fast answers to common questions without technical jargon.

### Common Workflows

| I Want To... | How to Invoke | What I Get |
|--------------|---------------|------------|
| **Process a VTT transcript** | `/transcript meeting.vtt` | 8 Markdown files + 2 mindmaps + quality review |
| **Analyze a SRT subtitle file** | `/transcript subtitles.srt` | Same as above, auto-detects SRT format |
| **Extract action items only** | "Find action items in meeting.vtt" | 04-action-items.md with assignees and due dates |
| **Get decisions made** | "What was decided in the meeting?" | 05-decisions.md with context and rationale |
| **Use a specific domain** | `/transcript standup.vtt --domain software-engineering` | Extraction tuned for engineering context |
| **Skip mindmap generation** | `/transcript meeting.vtt --no-mindmap` | 8 files + quality review (no visualizations) |
| **Higher quality extraction** | `/transcript meeting.vtt --model-extractor opus` | Better entity extraction, 3.75x cost |
| **Lower cost processing** | `/transcript meeting.vtt --model-extractor haiku` | Faster, 88% cost savings, lower quality |
| **ASCII-only mindmap** | `/transcript meeting.vtt --mindmap-format ascii` | Terminal-friendly visualization (no Mermaid) |
| **Resume failed processing** | Check `regeneration_command` in error output | Re-run from last checkpoint |

### What You Get (Output Files)

**Core Packet (8 files):**
```
transcript-{id}/
├── 00-index.md             ← Start here: Navigation + stats
├── 01-summary.md           ← Executive summary
├── 02-transcript.md        ← Full transcript with timestamps
├── 03-speakers.md          ← Speaker directory
├── 04-action-items.md      ← Action items with assignees
├── 05-decisions.md         ← Decisions with context
├── 06-questions.md         ← Open questions
├── 07-topics.md            ← Topic-based navigation
└── _anchors.json           ← Deep linking registry
```

**Mindmaps (default: both formats):**
```
08-mindmap/
├── mindmap.mmd             ← Mermaid diagram (rendered by tools)
└── mindmap.ascii.txt       ← ASCII art (terminal-friendly)
```

**Quality Assurance:**
```
quality-review.md           ← Validation results (>= 0.90 score)
```

### Processing Time Estimates

| Transcript Size | Segments | Duration | VTT (Python) | SRT/TXT (LLM) |
|-----------------|----------|----------|--------------|---------------|
| Small | < 500 | < 30 min | ~5 seconds | ~30 seconds |
| Medium | 500-2000 | 30-90 min | ~10 seconds | ~2 minutes |
| Large | 2000-5000 | 90-180 min | ~20 seconds | ~5 minutes |
| Very Large | > 5000 | > 3 hours | ~30 seconds | ~10 minutes |

**Note:** VTT files use deterministic Python parser (1,250x faster than LLM).
SRT and plain text files require LLM processing (slower but still sub-minute for most).

### Cost Estimates (Per 10,000 Input Tokens)

| Configuration | Estimated Cost | Quality Trade-off |
|---------------|----------------|-------------------|
| **Default (mixed)** | ~$0.12 | Balanced - recommended for most use cases |
| **All Haiku** | ~$0.015 | 88% savings, ~70-75% extraction accuracy |
| **All Sonnet** | ~$0.15 | Baseline quality, ~85-90% accuracy |
| **All Opus** | ~$0.75 | Highest quality (6x cost), ~95%+ accuracy |
| **Extractor Opus only** | ~$0.45 | Targeted quality boost (3.75x cost for extractions) |

**Cost Breakdown (Default):**
- ts-parser (haiku): ~$0.0025 - Simple orchestration
- ts-extractor (sonnet): ~$0.06 - Most token-intensive
- ts-formatter (sonnet): ~$0.03 - Template-based generation
- ts-mindmap-* (sonnet): ~$0.015 - Hierarchical reasoning
- ps-critic (sonnet): ~$0.015 - Quality evaluation

### Quality Thresholds

| Metric | Target | What It Means | How to Improve |
|--------|--------|---------------|----------------|
| Extraction precision | > 85% | % of extracted entities that are correct | Use `--model-extractor opus` |
| Extraction recall | > 85% | % of actual entities successfully extracted | Improve transcript quality (better audio) |
| Confidence threshold | >= 0.7 | Minimum confidence to include entity | Increase threshold for higher precision |
| Quality score | >= 0.90 | ps-critic aggregate validation score | Fix issues listed in quality-review.md |

### Troubleshooting Common Issues

| Problem | Likely Cause | Solution |
|---------|--------------|----------|
| "File not found" error | Incorrect path | Use absolute path or check working directory |
| Parsing fails (VTT) | Encoding issue | File may be UTF-16 (use `--format srt` to force LLM) |
| Low quality score | Poor transcript quality | Review quality-review.md for specific issues |
| Missing action items | Implicit language | Use `--model-extractor opus` for better semantic understanding |
| Mindmap syntax error | Mermaid validation failed | Check mindmap.mmd for plain text node requirement |
| ASCII mindmap too wide | Terminal width < 80 chars | Resize terminal or use Mermaid version |
| High cost | Using Opus for all agents | Switch to default or use `--model-extractor opus` only |
| Context window exceeded | File too large (rare) | Python chunker should prevent this; report as bug |

---

> Orchestration troubleshooting documentation: see [references/orchestration-troubleshooting.md](references/orchestration-troubleshooting.md)

---

> Cross-skill integration documentation: see [references/cross-skill-integration.md](references/cross-skill-integration.md)

---

## Related Documents

### Backlinks
- [TDD-transcript-skill.md](../../projects/PROJ-008-transcript-skill/work/EPIC-001-transcript-skill/FEAT-001-analysis-design/EN-005-design-documentation/docs/TDD-transcript-skill.md) - Architecture overview
- [TDD-FEAT-004](../../projects/PROJ-008-transcript-skill/work/EPIC-001-transcript-skill/FEAT-004-hybrid-infrastructure/docs/design/TDD-FEAT-004-hybrid-infrastructure.md) - Hybrid Infrastructure Technical Design (v2.0 basis)
- [ADR-001](../../projects/PROJ-008-transcript-skill/work/EPIC-001-transcript-skill/FEAT-001-analysis-design/EN-004-architecture-decisions/docs/adrs/adr-001.md) - Agent Architecture
- [ADR-002](../../projects/PROJ-008-transcript-skill/work/EPIC-001-transcript-skill/FEAT-001-analysis-design/EN-004-architecture-decisions/docs/adrs/adr-002.md) - Artifact Structure
- [ADR-006](../../docs/adrs/ADR-006-mindmap-pipeline-integration.md) - Mindmap Pipeline Integration (v2.1 basis)
- [DISC-009](../../projects/PROJ-008-transcript-skill/work/EPIC-001-transcript-skill/FEAT-002-implementation/EN-019-live-skill-invocation/DISC-009-agent-only-architecture-limitation.md) - Agent-Only Architecture Limitation (v2.0 rationale)
- [EN-025](../../projects/PROJ-008-transcript-skill/work/EPIC-001-transcript-skill/FEAT-004-hybrid-infrastructure/EN-025-skill-integration/EN-025-skill-integration.md) - v2.0 Integration Enabler
- [EN-026](../../projects/PROJ-008-transcript-skill/work/EPIC-001-transcript-skill/FEAT-003-future-enhancements/EN-026-token-based-chunking/EN-026-token-based-chunking.md) - Token-Based Chunking (BUG-001 fix)
- [DISC-001](../../projects/PROJ-008-transcript-skill/work/EPIC-001-transcript-skill/FEAT-003-future-enhancements/EN-026-token-based-chunking/EN-026--DISC-001-json-serialization-overhead.md) - JSON Serialization Overhead (~22%)

### Forward Links
- [PLAYBOOK.md](./docs/PLAYBOOK.md) - Execution playbook
- [RUNBOOK.md](./docs/RUNBOOK.md) - Operational procedures
- [VTT Parser](./src/parser/vtt_parser.py) - Python VTT parser (v2.0)
- [Transcript Chunker](./src/chunker/transcript_chunker.py) - Python chunker (v2.0)

---

## Routing Disambiguation

> When this skill is the wrong choice and what happens if misrouted.

| Condition | Use Instead | Consequence of Misrouting |
|-----------|-------------|--------------------------|
| Non-transcript file analysis (code, markdown, config files) | `/problem-solving` or Read tool directly | Transcript parsing agents (ts-parser, ts-extractor) applied to non-VTT/SRT files produce parsing failures; hybrid Python+LLM architecture expects transcript-format input |
| General text processing or summarization | `/problem-solving` (ps-analyst or ps-synthesizer) | Transcript agents apply speaker identification, timestamp extraction, and domain-specific entity extraction patterns that are irrelevant to general text; 1,250x cost multiplier if Task agents invoked unnecessarily vs. direct text processing |
| Requirements engineering or design work | `/nasa-se` | Transcript skill extracts meeting content; requirements formalization and V&V traceability require NASA-SE methodology |
| Adversarial quality review of deliverables | `/adversary` | Transcript agents score extraction quality against transcript-specific criteria, not the S-014 LLM-as-Judge rubric for deliverable quality |
| Research, analysis, or root cause investigation | `/problem-solving` | Transcript agents have no analytical methodology beyond extraction; research and causal investigation require ps-researcher or ps-investigator |
| Security assessment or threat modeling | `/eng-team` | Transcript skill has no security methodology; security-engineering domain context provides STRIDE/DREAD extraction but does not replace eng-team threat modeling |

---

## Agent Details

For detailed agent specifications, see:

- `agents/ts-parser.md` - Parser/Orchestrator agent definition (v2.0)
- `agents/ts-extractor.md` - Extractor agent definition
- `agents/ts-formatter.md` - Formatter agent definition
- `agents/ts-mindmap-mermaid.md` - Mermaid mindmap agent definition (ADR-006)
- `agents/ts-mindmap-ascii.md` - ASCII mindmap agent definition (ADR-006)
- `skills/problem-solving/agents/ps-critic.md` - Critic agent (shared)

---

## Document History

| Version | Date | Changes | Enabler/Task |
|---------|------|---------|--------------|
| 1.0.0 | 2026-01-26 | Initial SKILL.md with agent pipeline and basic invocation | FEAT-001 |
| 2.0.0 | 2026-01-30 | Hybrid Python+LLM architecture per DISC-009 findings | EN-025, DISC-009 |
| 2.1.0 | 2026-01-30 | Mindmap pipeline integration (default ON, opt-out via --no-mindmap) | ADR-006, EN-024 |
| 2.2.0 | 2026-01-29 | Explicit CLI invocation instructions for Phase 1 parsing | EN-024 (verification gap fix) |
| 2.3.0 | 2026-01-30 | Token-based chunking (fixes BUG-001 chunk token overflow) | EN-026, BUG-001 |
| 2.4.0 | 2026-01-30 | **EN-028 Compliance:** Added invoking section with natural language patterns, enhanced state passing with error handling, file persistence requirements (P-002 checklist), self-critique protocol (pre-finalization checks), restructured for triple-lens audience (L0/L1/L2), expanded Quick Reference with troubleshooting, model selection documentation (--model-* flags). | EN-028, TASK-407-411 |
| 2.4.1 | 2026-01-30 | **G-028 Iteration 2 Refinements (F-001 to F-005):** Added 5 error invocation examples with error outputs (F-001); documented error state structures for all agents including propagated errors (F-002); expanded recovery scenarios from 3 to 10 covering Python parser failure, context overflow, file write errors, quality gate failure, timeouts, partial extraction, mindmap failures, file conflicts, missing dependencies, and state corruption (F-003); added quantitative thresholds to all agent self-critique checklists with numeric bounds for validation (F-004); expanded Quick Reference troubleshooting section with 7 orchestration failure scenarios including pipeline stuck, agent timeout, quality gate immediate failure, file conflicts, mindmap partial failure, state key mismatch, and Python parser fallback issues (F-005). Target: raise G-028 score from 0.78 to ≥ 0.90. | EN-028, G-028 Iteration 2 |
| 2.4.2 | 2026-01-30 | **EN-030 Documentation Polish:** Added 6 comprehensive tool examples (Bash, Read, Write, Task, Glob, Grep) with execution evidence (TASK-416); Added 6 design rationale deep-dives covering hybrid architecture, chunking strategy, mindmap default-on, quality threshold 0.90, dual citation system, and P-003 compliance (TASK-417); Added 3 cross-skill integration sections for /problem-solving, /orchestration, and /nasa-se (TASK-418). Target: raise G-030 score from 0.83 to ≥ 0.95. | EN-030, TASK-416-418 |
| 2.5.0 | 2026-01-31 | **ADR-007 Model-Agnostic Output:** Added "Model-Agnostic Output Requirements (ADR-007)" section with MUST-CREATE (8 files), MUST-NOT-CREATE lists, anchor format rules, citation format, and navigation requirements. Ensures output consistency across Sonnet/Opus/Haiku models. FEAT-006 Phase 4 implementation. | ADR-007, FEAT-006 |

---

*Skill Version: 2.5.0*
*Architecture: Hybrid Python+LLM (Strategy Pattern) + Mindmap Generation + Token-Based Chunking*
*Constitutional Compliance: Tom Constitution v1.0 (P-001, P-002, P-003, P-004, P-010, P-020, P-022)*
*ADR Compliance: ADR-002 (packet structure), ADR-003 (anchor registry), ADR-004 (file splitting), ADR-006 (mindmap), ADR-007 (output template)*
*Created: 2026-01-26*
*Last Updated: 2026-01-31 (ADR-007 Model-Agnostic Output)*
