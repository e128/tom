# Model Selection and Profiles

> Extracted from `skills/transcript/SKILL.md` for progressive disclosure (Level 3).
> **Parent:** `skills/transcript/SKILL.md` § Model Selection, § Model Profiles

## Document Sections

| Section | Purpose |
|---------|---------|
| [Parameters](#parameters) | Per-agent model flags |
| [Cost Optimization](#cost-optimization) | Cost comparison by configuration |
| [Usage Examples](#usage-examples) | Economy, quality, balanced, custom modes |
| [Recommendations](#recommendations) | Per-agent model guidance |
| [Model Profiles](#model-profiles) | Quick-select configurations |
| [Priority Resolution](#priority-resolution) | Flag precedence rules |

---

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--model-parser` | haiku | Model for ts-parser (orchestration, routing) |
| `--model-extractor` | sonnet | Model for ts-extractor (entity extraction) |
| `--model-formatter` | sonnet | Model for ts-formatter (packet generation) |
| `--model-mindmap` | sonnet | Model for ts-mindmap-* (visualization) |
| `--model-critic` | sonnet | Model for ps-critic (quality review) |

**Valid Model Values:** `haiku`, `sonnet`, `opus`

## Cost Optimization

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

## Usage Examples

### Economy Mode (Minimize Cost)

```bash
uv run tom transcript parse meeting.vtt \
    --model-parser haiku \
    --model-extractor haiku \
    --model-formatter haiku \
    --model-mindmap haiku \
    --model-critic haiku
# Cost: ~$0.015 per 10K tokens
# Trade-off: Lower entity extraction accuracy (~70-75%)
```

### Quality Mode (Maximum Accuracy)

```bash
uv run tom transcript parse meeting.vtt \
    --model-extractor opus \
    --model-critic opus
# Cost: ~$0.45 per 10K tokens
# Trade-off: 3.75x cost increase, highest extraction accuracy (~95%+)
```

### Balanced Mode (Default)

```bash
uv run tom transcript parse meeting.vtt
# Cost: ~$0.12 per 10K tokens
# Trade-off: Optimal cost/quality balance (~85-90% accuracy)
```

### Custom Mix (Targeted Optimization)

```bash
uv run tom transcript parse meeting.vtt \
    --model-formatter haiku \
    --model-mindmap haiku
# Cost: ~$0.09 per 10K tokens
# Trade-off: 25% savings with minimal quality impact
```

## Recommendations

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

```bash
# Use economy profile
uv run tom transcript parse meeting.vtt --profile economy

# Use quality profile
uv run tom transcript parse meeting.vtt --profile quality

# Override individual models within a profile
uv run tom transcript parse meeting.vtt --profile economy --model-extractor opus
```

## Priority Resolution

Model selection follows this precedence (highest to lowest):

1. **Explicit `--model-*` flags** (highest priority)
2. **`--profile` flag**
3. **Default profile** (`balanced`)

### Cost Comparison

| Profile | Estimated Cost | vs. Balanced |
|---------|----------------|--------------|
| economy | ~$0.015 | **88% savings** |
| balanced (default) | ~$0.12 | Baseline |
| quality | ~$0.45 | 3.75x increase |
| speed | ~$0.015 | **88% savings** |

### When to Use Each Profile

| Profile | Use When |
|---------|----------|
| **economy** | High-volume batch, budget constraints, simple transcripts |
| **balanced** | General purpose, most workflows (recommended starting point) |
| **quality** | Critical/executive/legal meetings, poor transcription quality |
| **speed** | Real-time processing, quick turnaround, low-latency needs |
