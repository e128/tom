#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2026 Adam Nowak
"""Validate agent and skill YAML frontmatter against Claude Code's documented schemas.

Usage:
    uv run python scripts/validate-agent-frontmatter.py [OPTIONS] [FILES...]

Modes:
    agents (default)  Validate agent .md files against agent frontmatter schema
    skills            Validate SKILL.md files against skill frontmatter schema
    all               Validate both agents and skills

Examples:
    uv run python scripts/validate-agent-frontmatter.py
    uv run python scripts/validate-agent-frontmatter.py --mode skills
    uv run python scripts/validate-agent-frontmatter.py --mode all
    uv run python scripts/validate-agent-frontmatter.py skills/problem-solving/agents/*.md
"""

from __future__ import annotations

import argparse
import glob
import json
import re
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("ERROR: jsonschema not installed. Run: uv add --dev jsonschema", file=sys.stderr)
    sys.exit(1)

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: uv add --dev pyyaml", file=sys.stderr)
    sys.exit(1)


# --- Constants ---

AGENT_SCHEMA_PATH = Path("docs/schemas/claude-code-frontmatter-v1.schema.json")
SKILL_SCHEMA_PATH = Path("docs/schemas/claude-code-skill-frontmatter-v1.schema.json")

DEFAULT_AGENT_GLOBS = [
    "skills/*/agents/*.md",
    ".claude/agents/*.md",
]
DEFAULT_SKILL_GLOBS = [
    "skills/*/SKILL.md",
    ".claude/skills/*/SKILL.md",
]

# Official Claude Code fields (March 2026)
# Note: The CLI handler (_AGENT_KNOWN_FIELDS in
# src/agents/application/commands/validate_frontmatter_command.py)
# includes additional fields (effort, initialPrompt). Keep in sync.
AGENT_FIELDS = {
    "name",
    "description",
    "model",
    "tools",
    "disallowedTools",
    "mcpServers",
    "permissionMode",
    "maxTurns",
    "skills",
    "hooks",
    "memory",
    "background",
    "isolation",
    "color",
    "effort",
    "initialPrompt",
}
SKILL_FIELDS = {
    "name",
    "description",
    "argument-hint",
    "disable-model-invocation",
    "user-invocable",
    "allowed-tools",
    "model",
    "context",
    "agent",
    "hooks",
}

# YAML multiline indicators that Claude Code's skill indexer may misparse
MULTILINE_INDICATORS = re.compile(r"^description:\s*[>|]", re.MULTILINE)


# --- Frontmatter extraction ---


def extract_frontmatter(file_path: Path) -> dict | None:
    """Extract YAML frontmatter from a markdown file."""
    text = file_path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None
    return yaml.safe_load(match.group(1))


def extract_raw_frontmatter(file_path: Path) -> str | None:
    """Extract raw YAML frontmatter text (for multiline detection)."""
    text = file_path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    return match.group(1) if match else None


# --- Validation ---


def validate_agent(fm: dict, schema: dict, file_path: Path) -> tuple[list[str], list[str]]:
    """Validate agent frontmatter. Returns (errors, warnings)."""
    errors: list[str] = []
    warnings: list[str] = []

    # JSON Schema
    validator = jsonschema.Draft202012Validator(schema)
    for error in sorted(validator.iter_errors(fm), key=lambda e: list(e.path)):
        path = ".".join(str(p) for p in error.absolute_path) or "(root)"
        errors.append(f"  {path}: {error.message}")

    # Semantic: name matches filename
    expected_name = file_path.stem
    actual_name = fm.get("name", "")
    if actual_name != expected_name:
        errors.append(f"  name: '{actual_name}' does not match filename '{expected_name}'")

    # Semantic: jerry: prefix
    if actual_name.startswith("jerry:"):
        errors.append("  name: has 'jerry:' prefix — not used by Claude Code")

    # Semantic: unrecognized fields (warning, not error — Jerry-specific fields are expected)
    unknown = set(fm.keys()) - AGENT_FIELDS
    if unknown:
        warnings.append(
            f"  (root): unrecognized fields {sorted(unknown)} — "
            f"Claude Code ignores these. Move to .governance.yaml."
        )

    # Semantic: MCP tools in tools field
    tools = fm.get("tools")
    # Normalise comma-separated string format to list (PyYAML parses
    # "tools: Read, Write, Agent" as str, not list)
    if isinstance(tools, str):
        tools = [t.strip() for t in tools.split(",") if t.strip()]
    if isinstance(tools, list):
        mcp_tools = [t for t in tools if t.startswith("mcp__")]
        if mcp_tools:
            warnings.append(
                f"  tools: contains MCP tool names {mcp_tools} — use mcpServers field instead"
            )

        # STORY-022: P-003 — Agent/Task tool restricted to T5 orchestrators only.
        # The tools allowlist is the enforcement layer (DISC-001). If Agent or its
        # backward-compatible alias Task appears in a non-T5 agent's tools, that
        # agent can spawn subagents in violation of single-level nesting (H-01).
        delegation_tools = [t for t in tools if t in ("Agent", "Task")]
        if delegation_tools:
            # with_suffix replaces only the last suffix component.
            # All agent files use single .md suffix; multi-dot names
            # (e.g. agent.test.md) are not used in this codebase.
            gov_path = file_path.with_suffix(".governance.yaml")
            is_t5 = False
            if gov_path.exists():
                try:
                    gov = yaml.safe_load(gov_path.read_text(encoding="utf-8"))
                    if isinstance(gov, dict):
                        tier = gov.get("tool_tier")
                        is_t5 = isinstance(tier, str) and tier == "T5"
                except (yaml.YAMLError, OSError) as exc:
                    # fail closed: broken governance = not T5, but warn so
                    # engineers can diagnose why a legitimate T5 is failing
                    warnings.append(
                        f"  tools: could not read {gov_path.name}: {exc} — "
                        f"assuming non-T5 (fail closed)"
                    )
            if not is_t5:
                errors.append(
                    f"  tools: contains {delegation_tools} — only T5 orchestrator agents "
                    f"may have Agent/Task tool access (P-003 violation). "
                    f"Fix: remove {delegation_tools} from tools list, or set tool_tier: T5 "
                    f"in {gov_path.name} with documented justification."
                )

    return errors, warnings


def validate_skill(fm: dict, schema: dict, file_path: Path) -> tuple[list[str], list[str]]:
    """Validate SKILL.md frontmatter. Returns (errors, warnings)."""
    errors: list[str] = []
    warnings: list[str] = []

    # JSON Schema
    validator = jsonschema.Draft202012Validator(schema)
    for error in sorted(validator.iter_errors(fm), key=lambda e: list(e.path)):
        path = ".".join(str(p) for p in error.absolute_path) or "(root)"
        errors.append(f"  {path}: {error.message}")

    # Semantic: name matches directory
    expected_name = file_path.parent.name
    actual_name = fm.get("name", expected_name)
    if actual_name.lower() != expected_name:
        errors.append(f"  name: '{actual_name}' does not match directory '{expected_name}'")

    # Semantic: name case (must be lowercase)
    if actual_name != actual_name.lower():
        errors.append(f"  name: '{actual_name}' must be lowercase")

    # Semantic: unrecognized fields (warning, not error — Jerry-specific fields are expected)
    unknown = set(fm.keys()) - SKILL_FIELDS
    if unknown:
        warnings.append(
            f"  (root): unrecognized fields {sorted(unknown)} — "
            f"Claude Code ignores these (version, activation-keywords, agents, etc.)"
        )

    # Semantic: 'tools' used instead of 'allowed-tools'
    if "tools" in fm and "allowed-tools" not in fm:
        errors.append(
            "  tools: wrong field name — skills use 'allowed-tools', not 'tools'. "
            "'tools' is the agent field name and is unrecognized in SKILL.md."
        )

    # Semantic: multiline description indicator
    raw = extract_raw_frontmatter(file_path)
    if raw and MULTILINE_INDICATORS.search(raw):
        errors.append(
            "  description: uses YAML multiline indicator (> or |) — "
            "Claude Code's skill indexer may misparse this. Use single-line string."
        )

    # Semantic: MCP tools in allowed-tools (warning, not error)
    allowed = fm.get("allowed-tools")
    if isinstance(allowed, str):
        allowed = [t.strip() for t in allowed.split(",")]
    if isinstance(allowed, list):
        mcp_tools = [t for t in allowed if t.startswith("mcp__")]
        if mcp_tools:
            warnings.append(
                f"  allowed-tools: contains MCP tool names {mcp_tools} — "
                f"MCP tools may not be grantable via allowed-tools"
            )

    # Semantic: XML angle brackets in description (security)
    desc = fm.get("description", "")
    if isinstance(desc, str) and re.search(r"<[^>]+>", desc):
        errors.append(
            "  description: contains XML angle brackets — "
            "potential prompt injection risk per Anthropic Skill Guide"
        )

    return errors, warnings


# --- Main ---


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate agent/skill YAML frontmatter against Claude Code schemas."
    )
    parser.add_argument(
        "--mode",
        choices=["agents", "skills", "all"],
        default="agents",
        help="What to validate (default: agents)",
    )
    parser.add_argument(
        "--agent-schema",
        type=Path,
        default=AGENT_SCHEMA_PATH,
        help=f"Agent schema path (default: {AGENT_SCHEMA_PATH})",
    )
    parser.add_argument(
        "--skill-schema",
        type=Path,
        default=SKILL_SCHEMA_PATH,
        help=f"Skill schema path (default: {SKILL_SCHEMA_PATH})",
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="Specific files to validate (overrides --mode globs)",
    )
    args = parser.parse_args()

    total_errors = 0
    total_warnings = 0
    total_files = 0
    passed_files = 0

    # --- Agents ---
    if args.mode in ("agents", "all") or (args.files and not args.mode):
        if not args.agent_schema.exists():
            print(f"ERROR: Agent schema not found: {args.agent_schema}", file=sys.stderr)
            return 1
        agent_schema = json.loads(args.agent_schema.read_text(encoding="utf-8"))

        if args.files and args.mode == "agents":
            agent_files = [Path(f) for f in args.files]
        elif args.mode in ("agents", "all") and not args.files:
            agent_files = []
            for g in DEFAULT_AGENT_GLOBS:
                agent_files.extend(Path(p) for p in sorted(glob.glob(g)))
        else:
            agent_files = []

        if agent_files:
            print(f"--- Agents ({len(agent_files)} files) ---")
        for fp in agent_files:
            if not fp.exists():
                print(f"SKIP {fp} (not found)")
                continue
            fm = extract_frontmatter(fp)
            if fm is None:
                print(f"SKIP {fp} (no frontmatter)")
                continue
            total_files += 1
            errs, warns = validate_agent(fm, agent_schema, fp)
            if errs:
                print(f"FAIL {fp}")
                for e in errs:
                    print(e)
                for w in warns:
                    print(f"  WARN {w.lstrip()}")
                total_errors += len(errs)
                total_warnings += len(warns)
            elif warns:
                print(f"PASS {fp} (with warnings)")
                for w in warns:
                    print(f"  WARN {w.lstrip()}")
                passed_files += 1
                total_warnings += len(warns)
            else:
                print(f"PASS {fp}")
                passed_files += 1

    # --- Skills ---
    if args.mode in ("skills", "all"):
        if not args.skill_schema.exists():
            print(f"ERROR: Skill schema not found: {args.skill_schema}", file=sys.stderr)
            return 1
        skill_schema = json.loads(args.skill_schema.read_text(encoding="utf-8"))

        skill_files = []
        for g in DEFAULT_SKILL_GLOBS:
            skill_files.extend(Path(p) for p in sorted(glob.glob(g)))

        if skill_files:
            print(f"\n--- Skills ({len(skill_files)} files) ---")
        for fp in skill_files:
            if not fp.exists():
                print(f"SKIP {fp} (not found)")
                continue
            fm = extract_frontmatter(fp)
            if fm is None:
                print(f"SKIP {fp} (no frontmatter)")
                continue
            total_files += 1
            errs, warns = validate_skill(fm, skill_schema, fp)
            if errs:
                print(f"FAIL {fp}")
                for e in errs:
                    print(e)
                for w in warns:
                    print(f"  WARN {w.lstrip()}")
                total_errors += len(errs)
                total_warnings += len(warns)
            elif warns:
                print(f"PASS {fp} (with warnings)")
                for w in warns:
                    print(f"  WARN {w.lstrip()}")
                passed_files += 1
                total_warnings += len(warns)
            else:
                print(f"PASS {fp}")
                passed_files += 1

    # --- Summary ---
    print(f"\n{'=' * 60}")
    parts = [f"{passed_files}/{total_files} passed", f"{total_errors} errors"]
    if total_warnings:
        parts.append(f"{total_warnings} warnings")
    print(f"Results: {', '.join(parts)}")
    if total_errors > 0:
        print("FAILED")
        return 1
    if total_warnings > 0:
        print("ALL PASSED (with warnings)")
    else:
        print("ALL PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
