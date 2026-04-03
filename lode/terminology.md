# Terminology
*Updated: 2026-04-03T00:00:00Z*

Jerry-specific terms and their meanings. One term per line.

## Core Concepts

- **Jerry** — the framework itself; also the CLI tool name
- **Context Rot** — degradation of LLM performance as context window fills with accumulated tokens; the core problem Jerry solves
- **Lode** — the AI's structured persistent memory in `lode/`; named after a vein of ore (rich, structured deposit)
- **Lode Coding** — the methodology of keeping all project knowledge in `lode/` and treating the AI as the memory owner
- **HARD Rule** — a non-overridable governance constraint; identified by `H-XX` IDs (e.g., H-05, H-22)
- **MEDIUM Standard** — an overridable standard requiring documented justification to override
- **SOFT Guideline** — an optional suggestion requiring no justification to override

## Quality Framework

- **Quality Gate** — the 0.92 weighted composite score threshold required for C2+ deliverables
- **C1/C2/C3/C4** — criticality levels (Routine / Standard / Significant / Critical)
- **Creator-critic-revision cycle** — minimum 3-iteration quality loop required for C2+ work (H-14)
- **S-014** — LLM-as-Judge scoring strategy using 6 dimensions (completeness, consistency, rigor, evidence, actionability, traceability)
- **Context Rot** — also a specific auto-escalation concern; see AE-006 rules

## Skills and Agents

- **Skill** — a `/slash-command` capability; lives in `skills/{name}/SKILL.md`
- **Agent** — a specialized subagent; lives in `skills/{name}/agents/{agent}.md` with companion `.governance.yaml`
- **Trigger map** — the keyword-to-skill routing table in `mandatory-skill-usage.md`
- **T1–T5 tiers** — tool security tiers (T1=Read-Only, T2=Read-Write, T3=Persistent+MK, T4=External+Web, T5=Orchestration+Agent)
- **H-22** — the HARD rule mandating proactive skill invocation; violations require rework
- **Circuit breaker** — max 3 routing hops before halting and escalating to user (H-36)

## Work Tracking

- **PROJ-NNN** — project identifier pattern (e.g., `PROJ-024`)
- **EPIC/FEAT/STORY/TASK/BUG** — entity type hierarchy in the worktracker
- **WORKTRACKER.md** — the per-project work item index
- **WTI rules** — worktracker integrity rules (WTI-001 through WTI-009)
- **JERRY_PROJECT** — environment variable that must be set for active project (H-04)

## Architecture

- **Hexagonal architecture** — domain layer at center; application, infrastructure, interface layers surround it
- **Composition root** — the only place where infrastructure implementations are wired to domain ports
- **Port** — a domain-layer interface (e.g., `WorkItemRepository`)
- **Adapter** — an infrastructure-layer implementation of a port
- **H-07** — HARD rule enforcing layer isolation: domain must not import from infrastructure or interface

## Python Environment

- **UV** — the required Python package manager; `uv run`, `uv add`, `uv sync`
- **H-05** — HARD rule: MUST use `uv run` for all Python execution; NEVER `python`/`pip`/`pip3`
