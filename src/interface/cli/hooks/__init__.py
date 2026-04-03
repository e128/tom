# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2026 Adam Nowak

"""
Tom CLI Hooks Package.

Handlers for Claude Code hook events dispatched via the ``tom hooks``
CLI subcommand group.

Hook handlers:
    - HooksPromptSubmitHandler: Handles UserPromptSubmit events
    - HooksSessionStartHandler: Handles SessionStart events
    - HooksPreCompactHandler: Handles PreCompact events
    - HooksPreToolUseHandler: Handles PreToolUse events

References:
    - EN-006: tom hooks CLI Command Namespace
    - PROJ-004: Context Resilience
"""
