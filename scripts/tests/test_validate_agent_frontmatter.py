#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2026 Adam Nowak
"""Tests for validate-agent-frontmatter.py P-003 Agent tool check (STORY-022)."""

from __future__ import annotations

# Import the validation function under test
import importlib
from pathlib import Path

import pytest
import yaml

# The script uses a hyphenated filename, so import via importlib
spec = importlib.util.spec_from_file_location(
    "validate_agent_frontmatter",
    Path(__file__).parent.parent / "validate-agent-frontmatter.py",
)
vaf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vaf)


def _repo_root() -> Path:
    """Find repo root by walking up from this file to find pyproject.toml."""
    p = Path(__file__).resolve().parent
    while p != p.parent:
        if (p / "pyproject.toml").exists():
            return p
        p = p.parent
    return Path.cwd()


@pytest.fixture()
def agent_schema() -> dict:
    """Load the agent frontmatter schema."""
    import json

    schema_path = _repo_root() / "docs" / "schemas" / "claude-code-frontmatter-v1.schema.json"
    return json.loads(schema_path.read_text(encoding="utf-8"))


@pytest.fixture()
def tmp_agent(tmp_path: Path):
    """Factory for creating temp agent .md + .governance.yaml pairs."""

    def _create(
        name: str = "test-agent",
        tools: list[str] | None = None,
        tool_tier: str = "T2",
    ) -> Path:
        # Write .md frontmatter
        fm: dict = {"name": name, "description": f"Test agent {name}"}
        if tools is not None:
            fm["tools"] = tools
        md_path = tmp_path / f"{name}.md"
        md_content = f"---\n{yaml.dump(fm, default_flow_style=False)}---\n\nBody text.\n"
        md_path.write_text(md_content, encoding="utf-8")

        # Write .governance.yaml
        gov = {"version": "1.0.0", "tool_tier": tool_tier}
        gov_path = tmp_path / f"{name}.governance.yaml"
        gov_path.write_text(yaml.dump(gov), encoding="utf-8")

        return md_path

    return _create


class TestP003AgentToolCheck:
    """STORY-022: Error if non-T5 agent has Agent in tools."""

    def test_non_t5_agent_with_agent_tool_produces_error(
        self, agent_schema: dict, tmp_agent
    ) -> None:
        """Non-T5 agent with Agent in tools list MUST produce an error."""
        md_path = tmp_agent(tools=["Read", "Write", "Agent"], tool_tier="T2")
        fm = vaf.extract_frontmatter(md_path)
        errors, _ = vaf.validate_agent(fm, agent_schema, md_path)
        p003_errors = [e for e in errors if "P-003" in e]
        assert len(p003_errors) >= 1, f"Expected P-003 error, got: {errors}"

    def test_non_t5_agent_with_task_alias_produces_error(
        self, agent_schema: dict, tmp_agent
    ) -> None:
        """Non-T5 agent with Task (alias) in tools list MUST produce an error."""
        md_path = tmp_agent(tools=["Read", "Write", "Task"], tool_tier="T2")
        fm = vaf.extract_frontmatter(md_path)
        errors, _ = vaf.validate_agent(fm, agent_schema, md_path)
        p003_errors = [e for e in errors if "P-003" in e]
        assert len(p003_errors) >= 1, f"Expected P-003 error for Task alias, got: {errors}"

    def test_t5_agent_with_agent_tool_no_error(self, agent_schema: dict, tmp_agent) -> None:
        """T5 orchestrator with Agent in tools MUST NOT produce a P-003 error."""
        md_path = tmp_agent(
            name="ux-orchestrator",
            tools=["Read", "Write", "Agent"],
            tool_tier="T5",
        )
        fm = vaf.extract_frontmatter(md_path)
        errors, _ = vaf.validate_agent(fm, agent_schema, md_path)
        p003_errors = [e for e in errors if "P-003" in e]
        assert len(p003_errors) == 0, f"T5 agent should NOT get P-003 error: {p003_errors}"

    def test_agent_without_agent_tool_no_error(self, agent_schema: dict, tmp_agent) -> None:
        """Agent without Agent/Task in tools produces no P-003 error."""
        md_path = tmp_agent(tools=["Read", "Write", "Grep"], tool_tier="T2")
        fm = vaf.extract_frontmatter(md_path)
        errors, _ = vaf.validate_agent(fm, agent_schema, md_path)
        p003_errors = [e for e in errors if "P-003" in e]
        assert len(p003_errors) == 0, f"Should have no P-003 errors: {p003_errors}"

    def test_string_format_tools_with_agent_produces_error(
        self, agent_schema: dict, tmp_path: Path
    ) -> None:
        """Comma-separated string tools format MUST also be caught (FINDING-001)."""
        # PyYAML parses "tools: Read, Write, Agent" as a str, not list
        md_path = tmp_path / "string-tools-agent.md"
        md_content = "---\nname: string-tools-agent\ndescription: Test\ntools: Read, Write, Agent\n---\n\nBody.\n"
        md_path.write_text(md_content, encoding="utf-8")
        gov_path = tmp_path / "string-tools-agent.governance.yaml"
        gov_path.write_text("version: 1.0.0\ntool_tier: T2\n", encoding="utf-8")
        fm = vaf.extract_frontmatter(md_path)
        errors, _ = vaf.validate_agent(fm, agent_schema, md_path)
        p003_errors = [e for e in errors if "P-003" in e]
        assert len(p003_errors) >= 1, f"String-format tools should catch Agent: {errors}"

    def test_missing_governance_yaml_defaults_to_error(
        self, agent_schema: dict, tmp_path: Path
    ) -> None:
        """If governance.yaml is missing, Agent in tools MUST still error (fail-closed)."""
        fm = {"name": "no-gov-agent", "description": "No governance", "tools": ["Read", "Agent"]}
        md_path = tmp_path / "no-gov-agent.md"
        md_content = f"---\n{yaml.dump(fm, default_flow_style=False)}---\n\nBody.\n"
        md_path.write_text(md_content, encoding="utf-8")
        # No .governance.yaml created -- should fail closed
        fm_parsed = vaf.extract_frontmatter(md_path)
        errors, _ = vaf.validate_agent(fm_parsed, agent_schema, md_path)
        p003_errors = [e for e in errors if "P-003" in e]
        assert len(p003_errors) >= 1, "Missing governance should fail closed"
