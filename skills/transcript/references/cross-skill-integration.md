# Cross-Skill Integration

> Reference documentation for transcript skill integration with other Tom skills. Loaded on demand from SKILL.md.
> Covers: /problem-solving (ps-critic usage), /orchestration (multi-phase pipeline), /nasa-se (requirements traceability).

---

## Cross-Skill Integration: /problem-solving

The transcript skill integrates with the `/problem-solving` skill for quality validation.

### ps-critic Agent Usage

**What is ps-critic?**
- ps-critic is a **problem-solving agent** from the `/problem-solving` skill
- Role: Quality Inspector (validates transcript outputs against criteria)
- Specialization: Systematic review using 5W2H, Ishikawa, Pareto frameworks

**How transcript skill uses ps-critic:**

```
Phase 4: Quality Review
─────────────────────────
Invoke: ps-critic (from /problem-solving skill)
Input: All packet files (00-07) + mindmaps (08-)
Extension: skills/transcript/validation/ts-critic-extension.md
Threshold: 0.90
```

**Why ps-critic, not a transcript-specific validator?**
- **Reusability** - ps-critic validates ANY skill's outputs
- **Framework-driven** - Uses proven quality frameworks (5W2H, etc.)
- **Extensibility** - ts-critic-extension.md adds transcript-specific criteria

**Extension mechanism:**

```markdown
# ts-critic-extension.md (Transcript-Specific Criteria)

T-001: Timestamp completeness (>= 95% of segments have timestamps)
T-002: Speaker attribution (>= 90% of segments attributed)
T-003: Segment ordering (chronological order maintained)
T-004: Citation coverage (>= 95% of extractions have citations)
T-005: Confidence scores (>= 70% of extractions >= 0.7 confidence)
T-006: Token budget compliance (all files < 35K tokens)

MM-001: Mermaid syntax validation (mindmap is valid Mermaid)
MM-002: Deep link reference block (contains anchor mapping)

AM-001: ASCII line width (all lines <= 80 characters)
AM-002: Box drawing characters (UTF-8 box-drawing used correctly)
```

**See also:**
- [/problem-solving skill](../../../skills/problem-solving/SKILL.md) - Full documentation
- [ps-critic agent](../../../skills/problem-solving/agents/ps-critic.md) - Agent definition
- [ts-critic-extension.md](./validation/ts-critic-extension.md) - Transcript criteria

---

## Cross-Skill Integration: /orchestration

The transcript skill uses orchestration patterns from the `/orchestration` skill.

### Multi-Phase Pipeline Management

**What is /orchestration?**
- Framework for coordinating multi-agent workflows
- Provides sync barriers, state checkpointing, cross-pollinated pipelines
- Used when work has dependencies and requires coordination

**How transcript skill uses orchestration:**

```
Transcript Pipeline (v2.1):
──────────────────────────
Phase 1: Parse + Chunk     → ts-parser
  ↓ (Sync Barrier: Wait for index.json)
Phase 2: Extract Entities   → ts-extractor
  ↓ (Sync Barrier: Wait for extraction-report.json)
Phase 3: Format Packet      → ts-formatter
  ↓ (Sync Barrier: Wait for packet files)
Phase 3.5: Generate Mindmaps → ts-mindmap-*
  ↓ (Sync Barrier: Wait for mindmap files)
Phase 4: Quality Review     → ps-critic
```

**Orchestration patterns used:**

| Pattern | Usage in Transcript Skill |
|---------|---------------------------|
| **Sequential Phases** | 5 phases run in strict order |
| **State Passing** | Each phase outputs state for next |
| **Sync Barriers** | Wait for file existence before proceeding |
| **Graceful Degradation** | Mindmap failures don't block Phase 4 |
| **Checkpoint Recovery** | Can resume from any phase |

**Example: Sync Barrier Implementation**

```
After Phase 1 (ts-parser):
  ─────────────────────────
  1. Wait for index.json to exist
  2. Validate index.json schema
  3. IF valid: Proceed to Phase 2
  4. ELSE: Retry or abort
```

**See also:**
- [/orchestration skill](../../../skills/orchestration/SKILL.md) - Full documentation
- [ORCHESTRATION_PLAYBOOK.md](../../../skills/orchestration/docs/PLAYBOOK.md) - Step-by-step guide
- [Sync Barrier Pattern](../../../.claude/patterns/workflow/sync-barrier.md) - Pattern details

---

## Cross-Skill Integration: /nasa-se

The transcript skill applies NASA Systems Engineering principles for quality assurance.

### Requirements Traceability

**What is /nasa-se?**
- Framework based on NPR 7123.1D (NASA Systems Engineering)
- Provides verification & validation (V&V) processes
- Used for requirements traceability and quality gates

**How transcript skill uses NASA SE:**

```
Quality Gate (ps-critic Phase):
────────────────────────────────
Criterion T-004: Citation Coverage >= 95%

Traceable to:
  - REQ-EXT-003: "All extractions MUST include source citations"
  - PAT-004: Citation Required Pattern
  - ADR-003: Anchor Registry specification

Verification method:
  1. Count total extractions in extraction-report.json
  2. Count extractions with non-null citation field
  3. Calculate ratio: citations / total
  4. IF ratio >= 0.95: PASS
  5. ELSE: FAIL with specific missing citations list
```

**V&V Framework Application:**

| NASA SE Process | Transcript Skill Implementation |
|-----------------|--------------------------------|
| **Requirements Analysis** | ADR-002 (packet structure), ADR-003 (anchors) |
| **Design Verification** | Architecture tests (hexagonal compliance) |
| **Implementation Validation** | ps-critic quality review (0.90 threshold) |
| **Traceability** | Criterion → REQ → Pattern → Implementation |

**Quality Criteria Traceability Example:**

```
MM-001: Mermaid syntax validation
  ├─ Requirement: REQ-VIZ-001 (mindmaps must render correctly)
  ├─ Design: ADR-006 Section 5.3 (Mermaid syntax rules)
  ├─ Pattern: PAT-VIZ-001 (declarative visualization)
  ├─ Implementation: ts-mindmap-mermaid agent
  └─ Validation: ps-critic MM-001 criterion

Verification:
  1. Parse mindmap.mmd with Mermaid library
  2. Check for syntax errors
  3. Validate structure (root → branches → leaves)
  4. IF errors: FAIL (quality score penalty)
  5. ELSE: PASS
```

**See also:**
- [/nasa-se skill](../../../skills/nasa-se/SKILL.md) - Full documentation
- [NPR 7123.1D](../../../docs/standards/NPR-7123.1D.md) - NASA SE Handbook
- [V&V Framework](../../../skills/nasa-se/frameworks/verification-validation.md) - V&V processes

---
