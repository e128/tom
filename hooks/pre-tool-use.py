#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2026 Adam Nowak
"""PreToolUse hook wrapper. Delegates to jerry hooks pre-tool-use.

#150: Consolidated enforcement pipeline — SecurityEnforcementEngine
(blocked paths, dangerous commands, secrets/PII) + PreToolEnforcementEngine
(architecture V-038/V-041) + StalenessDetector, all via single CLI path.

Timeout budget: subprocess=4s < hooks.json=5s (1s buffer for wrapper overhead).
Fail-open: any exception results in exit 0 with no output (approve passthrough).
"""

import os
import subprocess
import sys
from pathlib import Path

root = os.environ.get("CLAUDE_PLUGIN_ROOT", str(Path(__file__).resolve().parent.parent))
try:
    result = subprocess.run(
        ["uv", "run", "--directory", root, "jerry", "--json", "hooks", "pre-tool-use"],
        input=sys.stdin.buffer.read(),
        capture_output=True,
        timeout=4,
    )
    sys.stdout.buffer.write(result.stdout)
    if result.stderr:
        sys.stderr.buffer.write(result.stderr)
    # Propagate CLI exit code when non-zero indicates a handled error
    # (vs. Exception path which is always fail-open)
    if result.returncode != 0:
        print(
            f"[hooks/pre-tool-use] CLI exited {result.returncode}",
            file=sys.stderr,
        )
except Exception:
    # Fail-open: timeout, FileNotFoundError, any other error
    # results in exit 0 with no stdout (approve passthrough)
    pass
sys.exit(0)
