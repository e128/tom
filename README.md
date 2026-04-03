# Tom Framework

> Behavior and workflow guardrails for Claude Code, with knowledge that accrues across sessions.

[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-blue.svg)](https://code.claude.com)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

## What is Tom?

Tom is a **Claude Code plugin** that adds structured problem-solving, multi-agent workflows, and persistent knowledge management to your sessions. It addresses **Context Rot** — the degradation of LLM performance as the context window fills — by persisting all work to files and loading selectively.

> "The effective context window where models perform optimally is often <256k tokens, far below advertised limits."
> — [Chroma Research](https://research.trychroma.com/context-rot)

## Quick Start

### Prerequisites

- [Claude Code](https://code.claude.com) 1.0.33+
- [Git](https://git-scm.com/)
- [uv](https://docs.astral.sh/uv/) (recommended — enables hooks for session context and quality enforcement)

### Install

```bash
# In Claude Code:
/plugin marketplace add e128/tom
/plugin install tom@tom-framework
```

> **Note:** The `owner/repo` shorthand clones via SSH. If you don't have SSH keys configured, use the full HTTPS URL: `/plugin marketplace add https://github.com/e128/tom.git`

See [docs/INSTALLATION.md](docs/INSTALLATION.md) for all installation methods, offline install, and troubleshooting.

### Verify

After installation, run `/plugin` in Claude Code. You should see `tom` in the **Installed** tab.

```
You: /problem-solving investigate why the auth tests are failing

Claude: I'll invoke ps-investigator to trace the root cause...
        [Applies 5 Whys methodology]
        [Creates persistent analysis artifact]

        Root cause: Token validation skips expiry check when
        issued_at is missing from JWT payload.

        Analysis saved to: projects/PROJ-001/investigations/auth-failure.md
```

## Skills

Tom provides skills — natural language interfaces invoked with slash commands or triggered automatically by keyword. Each skill has specialized agents that produce persistent file artifacts.

### Analysis & Research

| Skill | What It Does |
|-------|-------------|
| `/problem-solving` | Research, analysis, root cause investigation, code review (researcher, analyst, architect, investigator, critic, and more) |
| `/architecture` | Architecture decision records (ADRs) and design evaluation |

### Engineering & Security

| Skill | What It Does |
|-------|-------------|
| `/eng-team` | Secure software engineering — threat modeling, SDLC, SAST/DAST, code review, incident response |
| `/red-team` | Offensive security testing — reconnaissance, exploitation, privilege escalation, reporting |

### Quality & Governance

| Skill | What It Does |
|-------|-------------|
| `/adversary` | Adversarial quality reviews — red team analysis, devil's advocate, steelman, pre-mortem, tournament scoring |
| `/ast` | Markdown AST parsing, frontmatter validation, structural analysis |
| `/claude-revision` | Periodic health check for agents, skills, rules, and configuration |

### Documentation & Transcripts

| Skill | What It Does |
|-------|-------------|
| `/diataxis` | Four-quadrant documentation — tutorials, how-to guides, reference, explanation |
| `/transcript` | Parse meeting recordings (VTT, SRT, plain text) into structured packets with action items and decisions |

### Product & UX

| Skill | What It Does |
|-------|-------------|
| `/pm-pmm` | Product strategy, customer insight, business analysis, competitive intelligence, GTM planning |
| `/user-experience` | UX methodology — heuristic evaluation, JTBD, Kano model, design sprints, HEART metrics, inclusive design |
| `/use-case` | Use case authoring (Cockburn) and slicing (Jacobson UC 2.0) |
| `/test-spec` | BDD test specifications from use cases (Clark transformation) |
| `/contract-design` | API contract generation (OpenAPI 3.1) from use case artifacts |

### Prompt & Knowledge

| Skill | What It Does |
|-------|-------------|
| `/prompt-engineering` | Structured prompt construction, constraint generation, quality scoring |
| `/bootstrap` | Generate implementation references for any library, framework, or tool |

### Workflow & Tracking

| Skill | What It Does |
|-------|-------------|
| `/orchestration` | Multi-phase workflow coordination with quality gates and checkpointing |
| `/worktracker` | Local work item management — epics, features, stories, tasks, bugs |
| `/nasa-se` | Systems engineering processes per NPR 7123.1D — requirements, V&V, trade studies |

### Voice

| Skill | What It Does |
|-------|-------------|
| `/saucer-boy` | Session conversational voice (McConkey personality) |
| `/saucer-boy-framework-voice` | Framework output voice quality gate and persona compliance |

## How It Works

Tom uses a **single-level orchestrator-worker** architecture. When you invoke a skill, the main session acts as orchestrator and delegates to specialized agents — each running in its own isolated context window.

```
You: "Research OAuth2 patterns and create an ADR"

Main Session (orchestrator)
    |
    +-- ps-researcher  (surveys OAuth2 landscape)
    +-- ps-analyst     (compares approaches)
    +-- ps-architect   (produces ADR with trade-offs)
    +-- ps-critic      (adversarial quality review)
```

All artifacts are **persisted to files** — they survive context compaction and build your project's knowledge base across sessions.

### Quality Enforcement

For important deliverables, Tom applies a multi-pass quality cycle:

1. **Creator** produces the artifact
2. **Critic** applies adversarial review (devil's advocate, steelman, red team)
3. **Revision** addresses findings
4. Repeat until quality threshold is met (default >= 0.92)

## Platform Support

Tom is primarily developed on macOS. CI tests run on all three platforms.

| Platform | Status |
|----------|--------|
| **macOS** | Fully supported |
| **Linux** | Expected to work — CI-tested on Ubuntu |
| **Windows** | Core functionality works — edge cases may exist with hooks and symlinks |

**Platform issue?** File a report:
[macOS](https://github.com/e128/tom/issues/new?template=macos-compatibility.yml) |
[Linux](https://github.com/e128/tom/issues/new?template=linux-compatibility.yml) |
[Windows](https://github.com/e128/tom/issues/new?template=windows-compatibility.yml)

## Known Limitations

- **Skill definitions are large.** Most exceed the recommended 250-line limit. Decomposition into reference sub-files is in progress (transcript skill reduced 49% in v0.30.0).
- **Windows hook support is partial.** Hooks using symlinks or path-sensitive operations may behave differently. See [Platform Support](#platform-support).
- **No official Anthropic marketplace listing.** Tom is a community plugin installed from GitHub.

## Documentation

| Document | Purpose |
|----------|---------|
| [Installation Guide](docs/INSTALLATION.md) | All install methods, offline setup, troubleshooting |
| [CLAUDE.md](CLAUDE.md) | Session context — constraints, navigation, skill reference |
| [AGENTS.md](AGENTS.md) | Registry of all specialized agents |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Development setup and contribution guidelines |
| [CHANGELOG.md](CHANGELOG.md) | Release history |

## For Contributors

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

```bash
git clone https://github.com/e128/tom.git
cd tom
uv sync
uv run pytest
```

> **Note:** You do NOT need Python to use Tom as a plugin. Python and uv are only required for contributing to Tom's development or enabling hooks.

## References

- [Claude Code Documentation](https://code.claude.com/docs/en/quickstart)
- [Claude Code Plugins](https://code.claude.com/docs/en/discover-plugins)
- Chroma. "[Context Rot Research](https://research.trychroma.com/context-rot)"
- Cockburn, A. (2005). "[Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/)"

## License

Apache-2.0 — See [LICENSE](LICENSE) and [NOTICE](NOTICE) for details.
