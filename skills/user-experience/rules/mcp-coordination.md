# MCP Coordination Rules

<!-- STUB: Created during PROJ-022 Foundation phase. Full implementation in EPIC-001. -->

> MCP tool coordination rules for the /user-experience skill. Defines Figma, Miro, and Context7 integration patterns with graceful degradation fallbacks.

## Document Sections

| Section | Purpose |
|---------|---------|
| [MCP Dependency Matrix](#mcp-dependency-matrix) | Which sub-skills require which MCP servers |
| [Degraded Mode Behavior](#degraded-mode-behavior) | Fallback paths when MCP is unavailable |
| [Context7 Usage](#context7-usage) | When to use Context7 for UX framework docs |
| [Future MCP Adapters](#future-mcp-adapters) | Architecture for Figma/Miro adapters |

---

## MCP Dependency Matrix

<!-- TODO (EPIC-001): Define full MCP dependency matrix from SKILL.md spec. -->
<!-- Source: SKILL.md Section "MCP Integration Architecture" and issue #138 comment-2. -->

Pending implementation. MCP dependencies by category:

| Category | MCP Server | Sub-Skills | Status |
|----------|-----------|------------|--------|
| REQ (Required) | Context7 | All research-capable agents | Available |
| OPT (Optional) | Figma MCP | ux-atomic-architect, ux-sprint-facilitator | Not yet available |
| OPT (Optional) | Miro MCP | ux-sprint-facilitator, ux-lean-ux-facilitator | Not yet available |

---

## Degraded Mode Behavior

<!-- TODO (EPIC-001): Define fallback behavior when OPT/COND MCP servers are unavailable. -->

Pending implementation. When OPT MCP unavailable:
- Sub-skill operates on markdown-only artifacts
- Output quality may be reduced but sub-skill remains functional
- P-022: Agent discloses MCP unavailability to user

---

## Context7 Usage

<!-- TODO (EPIC-001): Define Context7 usage patterns for UX framework documentation lookup. -->

Pending implementation. Follows MCP-001 from `mcp-tool-standards.md`.

---

## Future MCP Adapters

<!-- TODO (EPIC-001): Define adapter architecture for Figma and Miro MCP servers. -->

Pending implementation. Architecture + fallback paths only; actual adapter implementation is out of scope for PROJ-022.

---

*Rule file: mcp-coordination.md*
*Parent skill: /user-experience*
*Created: 2026-03-03*
*Status: STUB — Full implementation tracked in EPIC-001*
