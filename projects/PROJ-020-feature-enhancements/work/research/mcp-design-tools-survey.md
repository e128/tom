# MCP Design Tools Ecosystem Survey

> Comprehensive survey of Model Context Protocol (MCP) servers for design and UX tools, assessing existing integrations and feasibility of creating new MCP adapters for a Tiny Team (2-3 people + AI) UX workflow.

## Document Sections

| Section | Purpose |
|---------|---------|
| [L0: Executive Summary](#l0-executive-summary) | Key findings, counts, top integrations for Tiny Teams |
| [L1: Tool-by-Tool Assessment](#l1-tool-by-tool-assessment) | Detailed per-tool MCP status, API, feasibility, value |
| [L1.1: Figma](#11-figma--uiux-design-prototyping-design-systems) | Official MCP + community servers |
| [L1.2: Miro](#12-miro--whiteboarding-journey-mapping-collaboration) | Official MCP server |
| [L1.3: Sketch](#13-sketch--ui-design-macos) | Community MCP servers |
| [L1.4: Adobe XD](#14-adobe-xd--uiux-design-prototyping) | Community MCP + Adobe ecosystem |
| [L1.5: InVision](#15-invision--prototyping-design-collaboration) | Discontinued platform |
| [L1.6: Maze](#16-maze--user-testing-usability-testing) | No MCP, limited API |
| [L1.7: Hotjar](#17-hotjar--heatmaps-session-recordings-user-behavior) | Third-party MCP via Zapier/Pipedream |
| [L1.8: Storybook](#18-storybook--component-library-documentation) | Official addon + community MCP |
| [L1.9: Zeroheight](#19-zeroheight--design-system-documentation) | Official MCP server |
| [L1.10: Framer](#110-framer--interactive-prototyping-web-design) | Official Server API + MCP |
| [L1.11: Penpot](#111-penpot--open-source-design-tool) | Official MCP (experimental) |
| [L1.12: Whimsical](#112-whimsical--wireframing-flowcharts) | Community MCP server |
| [L1.13: UserTesting](#113-usertesting--remote-user-testing-platform) | REST API, no MCP |
| [L1.14: Optimal Workshop](#114-optimal-workshop--information-architecture-testing) | No public API or MCP |
| [L1.15: Lookback](#115-lookback--user-research-platform) | No public API or MCP |
| [L1.16: Abstract](#116-abstract--design-version-control) | Legacy platform, no MCP |
| [L1.17: Lottie/LottieFiles](#117-lottielottiefiles--animation) | Community MCP server |
| [L1.18: Rive](#118-rive--animation-tool) | Official MCP (Early Access) |
| [L1.19: Principle](#119-principle--animation-prototyping) | No API or MCP |
| [L1.20: Axure](#120-axure--advanced-prototyping-documentation) | Legacy API, no MCP |
| [L1.21: Balsamiq](#121-balsamiq--low-fidelity-wireframing) | No MCP; Frame0 alternative |
| [Summary Matrix](#summary-matrix) | Consolidated comparison table |
| [L2: Integration Architecture](#l2-integration-architecture) | Tier model, priority roadmap, workflow patterns |
| [References](#references) | All sources with URLs |

---

## L0: Executive Summary

### What Was Researched and Why It Matters

This survey examined 20 design and UX tools to determine which have existing MCP (Model Context Protocol) server integrations and which could feasibly have MCP adapters built for them. The goal is to identify which tool integrations would most benefit a Tiny Team (2-3 people + AI) running UX workflows where AI agents need to interact with design artifacts, user research data, and component libraries.

### Key Counts

| Category | Count | Tools |
|----------|-------|-------|
| **Official/First-Party MCP Server** | 7 | Figma, Miro, Storybook, Zeroheight, Framer, Penpot, Rive |
| **Community/Third-Party MCP Server** | 5 | Sketch, Adobe XD, Whimsical, Hotjar (via Zapier/Pipedream), LottieFiles |
| **API Available (MCP Feasible)** | 3 | Maze, UserTesting, Axure (legacy) |
| **No API / No MCP / Discontinued** | 5 | InVision (shut down), Principle, Optimal Workshop, Lookback, Abstract |
| **Total with some MCP path** | 15 out of 20 | |

### Top 5 Most Critical Integrations for Tiny Teams

1. **Figma** (EXISTING MCP -- Official + Community) -- The centerpiece of modern UX design. Multiple MCP servers exist: official Dev Mode MCP for design-to-code, Framelink for layout context, and Cursor Talk to Figma for bidirectional read/write. A Tiny Team can have AI generate code directly from Figma designs, extract design tokens, and even create/modify design elements.

2. **Storybook** (EXISTING MCP -- Official Addon) -- Essential for component-driven development. The official `@storybook/addon-mcp` exposes component APIs, stories, and props to AI agents. For a Tiny Team sharing design system responsibilities, this enables AI to generate components that match documented patterns.

3. **Miro** (EXISTING MCP -- Official) -- The collaboration hub for UX workflows. Miro's MCP server enables AI agents to read board content (PRDs, journey maps, research), generate diagrams from code, and transform visual information into development artifacts. Built in collaboration with Anthropic, AWS, GitHub, and Google.

4. **Zeroheight** (EXISTING MCP -- Official) -- Design system documentation platform. The MCP server provides AI agents access to styleguides, design tokens, and component usage guidelines. For Tiny Teams, this means AI-generated code stays aligned with design system standards automatically.

5. **Hotjar** (EXISTING MCP -- Third-Party via Zapier/Pipedream) -- User behavior analytics. While not an official MCP, the Zapier/Pipedream MCP bridges enable AI agents to query survey responses and user behavior data. Critical for data-informed UX decisions in a Tiny Team where dedicated researchers are scarce.

### Key Takeaways

- **The MCP design ecosystem matured rapidly in 2025-2026.** Seven of 20 tools surveyed have official first-party MCP servers, up from near-zero in early 2025. Figma and Miro lead with the most capable implementations.
- **Read-heavy, write-limited.** Most MCP servers (and underlying APIs) are optimized for reading design data -- extracting tokens, layouts, component specs. Full bidirectional control (creating/modifying design elements) is available only through Figma's plugin-based MCP (Cursor Talk to Figma) and Penpot's experimental MCP.
- **User research tools lag behind.** Design tools (Figma, Miro, Framer) have strong MCP coverage. User research platforms (Maze, UserTesting, Optimal Workshop, Lookback) have minimal or no API/MCP support, creating a significant gap in AI-assisted UX workflows.
- **Open-source Penpot is a dark horse.** With an official (experimental) MCP server and a design-as-code philosophy, Penpot offers the most promising path for deep AI integration without vendor lock-in.
- **For Tiny Teams: prioritize Figma + Storybook + Miro + Zeroheight.** These four form a complete AI-augmented design-to-code pipeline with existing, production-ready MCP servers.

---

## L1: Tool-by-Tool Assessment

### 1.1 Figma -- UI/UX Design, Prototyping, Design Systems

**Status: EXISTING MCP (Multiple Servers)**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | Yes -- multiple implementations |
| **API Available?** | REST API (read-heavy), Plugin API (read+write), Webhooks |
| **MCP Feasibility** | N/A -- already exists |
| **Tiny Team Value** | **Critical** |

#### MCP Server Implementations

| Server | Maintainer | Key Capabilities |
|--------|-----------|-----------------|
| **Figma Dev Mode MCP** | Figma (official) | Exposes live layer structure -- hierarchy, auto-layout, variants, text styles, token references. Tools: `get_design_context` (React+Tailwind representation), `get_variable_defs` (tokens extraction). Read-only. |
| **Framelink / Figma-Context-MCP** | GLips (community) | Processes Figma API responses into simplified formats. Tools: `get_figma_data` (layout/styling), `download_figma_images` (asset export). Read-only. |
| **Cursor Talk to Figma** | Grab (community) | Bidirectional -- read designs AND modify them. Supports ~20 operations: shape creation, text modification, color adjustments, component management. Uses WebSocket bridge + Figma plugin. |
| **Figma Console MCP** | Southleft (community) | Turns design system into a living API. |

#### API Capabilities

- **REST API**: Read file structure, nodes, components, styles, design tokens, images. Export assets (PNG, SVG, PDF). Manage comments. Webhooks for file/project/team events. Granular scopes (file_content:read, file_metadata:read).
- **Plugin API**: Full read+write access to the canvas -- create/modify shapes, text, frames, components. Requires Figma app running.
- **Limitations**: REST API is primarily read-only for design elements. Write operations for design elements require the Plugin API or Cursor Talk to Figma MCP bridge.

#### Integration Patterns for AI Agents

- **Design-to-Code**: Agent reads Figma layout via MCP, generates framework-specific code (React, Vue, Tailwind).
- **Design Token Extraction**: Agent extracts color, spacing, typography tokens and generates CSS/JSON theme files.
- **Asset Export**: Agent exports icons, illustrations as SVG/PNG for development.
- **Design Modification**: Via Cursor Talk to Figma, agent can create wireframes, adjust layouts, apply style changes.
- **Design Review**: Agent reads design and checks against documented design system rules.

**Sources:**
1. [Figma MCP Server Guide](https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server) -- Official Figma documentation
2. [Introducing Figma MCP Server](https://www.figma.com/blog/introducing-figma-mcp-server/) -- Figma blog announcement
3. [Figma-Context-MCP GitHub](https://github.com/GLips/Figma-Context-MCP) -- Community MCP implementation
4. [Cursor Talk to Figma](https://github.com/grab/cursor-talk-to-figma-mcp) -- Bidirectional MCP by Grab
5. [Figma REST API Introduction](https://developers.figma.com/docs/rest-api/) -- Official API docs

---

### 1.2 Miro -- Whiteboarding, Journey Mapping, Collaboration

**Status: EXISTING MCP (Official)**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | Yes -- official Miro MCP server (public beta) |
| **API Available?** | REST API v2, OAuth 2.0, Webhooks |
| **MCP Feasibility** | N/A -- already exists |
| **Tiny Team Value** | **Critical** |

#### MCP Server Capabilities

The official Miro MCP server was built in collaboration with Anthropic, AWS, GitHub, Google, and Windsurf. It provides:

- **Read board content**: Access PRDs, design specs, user research, architecture diagrams, journey maps.
- **Generate diagrams**: Create diagrams from code or text descriptions directly on Miro boards.
- **Transform visual info**: Convert visual information (diagrams, maps) into code and structured formats.
- **Context-aware code generation**: PRDs, design specs, and user research from Miro become direct input for AI coding.

Supported AI clients: Claude Code, AWS Kiro, GitHub Copilot, Gemini CLI, Windsurf, Cursor, Lovable, Replit, OpenAI Codex, VS Code, Devin.

#### API Capabilities

- Full CRUD operations on boards, items (sticky notes, shapes, text, images, frames, connectors).
- Board content search and filtering.
- User and team management.
- Webhooks for real-time event notifications.

#### Integration Patterns for AI Agents

- **Journey Map Analysis**: Agent reads journey map from Miro, identifies pain points, generates UX recommendations.
- **PRD to Requirements**: Agent reads PRD on Miro board, extracts structured requirements.
- **Architecture Diagram Generation**: Agent generates architecture diagrams from codebase analysis.
- **Workshop Facilitation**: Agent creates structured brainstorming templates on Miro boards.

**Sources:**
1. [Miro MCP Documentation](https://developers.miro.com/docs/miro-mcp) -- Official developer docs
2. [Miro MCP Help Center](https://help.miro.com/hc/en-us/articles/31624028247058-Miro-MCP-Server-overview) -- Admin and setup guide
3. [Miro MCP Blog Announcement](https://miro.com/blog/bringing-organizational-context-to-ai-with-miro-mcp/) -- Strategic context

---

### 1.3 Sketch -- UI Design (macOS)

**Status: EXISTING MCP (Community)**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | Yes -- community implementations |
| **API Available?** | JavaScript API (plugins), file format parseable (.sketch is ZIP) |
| **MCP Feasibility** | N/A -- already exists |
| **Tiny Team Value** | **Low** (Figma has largely superseded Sketch for new teams) |

#### MCP Server Implementations

| Server | Capabilities |
|--------|-------------|
| **Sketch-Context-MCP** (jshmllr) | Parse .sketch files, extract design components, layout information, layer data. Provides structured data for AI code generation. |
| **sketch-mcp-server** (mater1996) | Similar file parsing and component extraction. |

#### Limitations

- Sketch is macOS-only, limiting team flexibility.
- Community MCP servers parse exported .sketch files; no live bidirectional connection.
- Sketch's market share has declined significantly vs. Figma.
- No official Sketch MCP server from the Sketch team.

#### Integration Patterns for AI Agents

- **Legacy File Migration**: Agent parses .sketch files to extract design tokens for migration to Figma.
- **Design Audit**: Agent reads Sketch components and checks for consistency.

**Sources:**
1. [Sketch-Context-MCP GitHub](https://github.com/jshmllr/sketch-context-mcp) -- Community MCP
2. [Sketch MCP Server LobeHub](https://lobehub.com/mcp/mater1996-sketch-mcp-server) -- Alternative implementation

---

### 1.4 Adobe XD -- UI/UX Design, Prototyping

**Status: EXISTING MCP (Community) + Adobe Ecosystem MCP**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | Yes -- community Adobe XD MCP + broader Adobe suite MCP |
| **API Available?** | Plugin API, XD file reading. Adobe Express has official MCP. |
| **MCP Feasibility** | N/A -- community MCP exists |
| **Tiny Team Value** | **Low** (Adobe XD development has slowed; Figma dominance) |

#### MCP Server Implementations

| Server | Capabilities |
|--------|-------------|
| **adobe-xd-mcp** (dekdee) | Read XD files, extract design tokens, analyze components, export design systems. Tools: `read_xd_file`, `extract_design_tokens`, `analyze_components`, `export_design_system`. React component generation. |
| **Adobe Creative Suite MCP** (matrayu) | Unified MCP for Photoshop, Premiere Pro, Illustrator, InDesign. Control Adobe apps via AI. |
| **Adobe Express Developer MCP** (Official Adobe) | Official, production-ready MCP for Adobe Express add-on development. npm: `@adobe/express-developer-mcp`. |

#### Key Consideration

Adobe's strategic direction is toward Adobe Express (with official MCP support) rather than XD. Teams starting new should prefer Figma over XD.

**Sources:**
1. [Adobe XD MCP LobeHub](https://lobehub.com/mcp/yourusername-adobe-xd-mcp) -- Community listing
2. [Adobe Express Developer MCP](https://developer.adobe.com/express/add-ons/docs/guides/getting_started/local_development/mcp_server/) -- Official Adobe docs
3. [Adobe Creative Suite MCP GitHub](https://github.com/matrayu/adobe-mcp) -- Unified Adobe MCP

---

### 1.5 InVision -- Prototyping, Design Collaboration

**Status: NOT FEASIBLE (Discontinued)**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | No (Zapier MCP for InVision Community forums only) |
| **API Available?** | No -- service shut down December 31, 2024 |
| **MCP Feasibility** | Not Feasible |
| **Tiny Team Value** | **None** |

InVision shut down its software services as of December 31, 2024. The Freehand product was sold to Miro. There is no viable path for MCP integration. Teams should migrate to Figma or Miro.

**Sources:**
1. [InVision Shutting Down - LogRocket](https://blog.logrocket.com/ux-design/invision-shutting-down/) -- Shutdown announcement

---

### 1.6 Maze -- User Testing, Usability Testing

**Status: FEASIBLE MCP (Medium difficulty)**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | No |
| **API Available?** | Limited -- integrations via Figma, Slack, Jira, Google Calendar, Miro. No public REST API for test results. |
| **MCP Feasibility** | Medium -- would require partnership or screen-scraping |
| **Tiny Team Value** | **High** |

#### API Capabilities (Limited)

- Figma integration for prototype import (one-click).
- Automated report generation and embedding in FigJam.
- Integration with Amplitude for analytics.
- Slack notifications for project updates.
- No documented public REST API for programmatic access to test results, heatmaps, or session data.

#### Integration Patterns (If MCP Were Built)

- **Test Results Analysis**: Agent reads usability test metrics (misclicks, time-on-screen, task success rates) and generates UX improvement recommendations.
- **Insight Extraction**: Agent processes open-ended responses and AI-generated themes.
- **Automated Reporting**: Agent pulls test summaries into design documentation.

#### Feasibility Assessment

Building an MCP adapter would require Maze to expose a public API or using browser automation (Playwright MCP) to extract data from the Maze dashboard. Without a public API, feasibility is limited to what can be accessed via the Figma+Maze integration or webhook-style notifications.

**Sources:**
1. [Maze Platform](https://maze.co/platform/user-testing/) -- Product overview
2. [Maze Integrations](https://maze.co/integrations/) -- Available integrations
3. [Maze API Tracker](https://apitracker.io/a/maze-design) -- API availability status

---

### 1.7 Hotjar -- Heatmaps, Session Recordings, User Behavior

**Status: EXISTING MCP (Third-Party via Zapier/Pipedream)**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | Yes -- via Zapier MCP and Pipedream MCP bridges |
| **API Available?** | REST API (limited): User Lookup API, Responses API, Events API. OAuth. Rate limit: 3000 req/min. |
| **MCP Feasibility** | N/A -- third-party MCP exists; custom MCP highly feasible |
| **Tiny Team Value** | **High** |

#### API Capabilities

| API | Access Level | Capabilities |
|-----|-------------|-------------|
| **Events API** | JavaScript (client-side) | Send custom events to Hotjar; filter recordings/heatmaps by events. |
| **Responses API** | REST (Ask Scale plan) | Export survey responses programmatically. |
| **User Lookup API** | REST (Observe/Ask Scale) | User lookup and GDPR deletion requests. |

#### MCP Implementations

- **Zapier Hotjar MCP**: Connects Hotjar actions to any MCP-compatible AI tool without custom code.
- **Pipedream Hotjar MCP**: OAuth-based connection, exposes Hotjar actions as MCP tools.

#### Limitations

- Cannot export heatmap images or session recording videos via API.
- API focuses on survey responses and user management, not behavioral analytics data.
- Heatmap data cannot be triggered by Events API (only filtered).

#### Integration Patterns for AI Agents

- **Survey Analysis**: Agent retrieves survey responses via API, identifies themes and sentiment patterns.
- **Event-Based Insights**: Agent queries event data to correlate user behavior with design changes.
- **GDPR Automation**: Agent processes user deletion requests.

**Sources:**
1. [Hotjar API Reference](https://help.hotjar.com/hc/en-us/articles/36820005914001-Hotjar-API-Reference) -- Official API docs
2. [Hotjar MCP via Zapier](https://zapier.com/mcp/hotjar) -- Zapier MCP bridge
3. [Hotjar MCP via Pipedream](https://mcp.pipedream.com/app/hotjar) -- Pipedream MCP bridge
4. [Hotjar Events API](https://help.hotjar.com/hc/en-us/articles/36819965075473-Events-API-Reference) -- Events reference

---

### 1.8 Storybook -- Component Library Documentation

**Status: EXISTING MCP (Official Addon + Community)**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | Yes -- official addon + multiple community implementations |
| **API Available?** | N/A (Storybook is a dev tool; MCP exposes its data directly) |
| **MCP Feasibility** | N/A -- already exists |
| **Tiny Team Value** | **Critical** |

#### MCP Server Implementations

| Server | Maintainer | Capabilities |
|--------|-----------|-------------|
| **@storybook/addon-mcp** | Storybook (official) | Runs MCP server within Storybook. Exposes component APIs, stories, props. Auto-generates and links example stories for new components. |
| **storybook-mcp** (mcpland) | Community | Interacts with Storybook docs, extracts component info, props data, icons, color palettes. Browser automation + JS execution. |
| **storybook-mcp-server** (stefanoamorelli) | Community | AI assistant access to components, stories, properties, screenshots. TypeScript + MCP SDK. |

#### Integration Patterns for AI Agents

- **Component Discovery**: Agent queries available components and their props to use correct patterns in generated code.
- **Story Generation**: Agent automatically creates Storybook stories for new components.
- **Design System Enforcement**: Agent checks generated code against documented component APIs.
- **Visual Testing**: Agent captures component screenshots and compares against baseline.

**Sources:**
1. [Storybook Addon MCP](https://storybook.js.org/addons/@storybook/addon-mcp) -- Official addon page
2. [Storybook MCP GitHub](https://github.com/storybookjs/mcp) -- Official repository
3. [storybook-mcp npm](https://www.npmjs.com/package/@storybook/addon-mcp) -- npm package

---

### 1.9 Zeroheight -- Design System Documentation

**Status: EXISTING MCP (Official)**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | Yes -- official `@zeroheight/mcp-server` |
| **API Available?** | REST API (Content API for docs), OAuth |
| **MCP Feasibility** | N/A -- already exists |
| **Tiny Team Value** | **High** |

#### MCP Server Capabilities

- **get-page**: Fetch guidance from a specific design system page -- usage notes, recommendations, supporting context.
- Local and remote server modes (local for desktop clients, remote for cloud-based AI tools).
- Requires Client ID and Access Token.
- Latest version: 2.1.1 (npm: `@zeroheight/mcp-server`).
- Compatible with Claude Desktop, VS Code, Cursor, and other MCP-compatible tools.

#### API Capabilities

- Content API for reading and pushing design system documentation.
- Custom plugin development support.
- LLM training data export.

#### Integration Patterns for AI Agents

- **Design System Compliance**: Agent reads component guidelines from Zeroheight before generating code, ensuring adherence to documented patterns.
- **Token Resolution**: Agent resolves design token references to actual values.
- **Documentation-Driven Development**: Agent uses Zeroheight docs as the source of truth for UI generation.

#### Notable: Figma Make + Zeroheight

Figma expanded Figma Make (Feb 2026) with a certified Zeroheight connector, enabling AI-powered prototypes to pull context from design system documentation directly.

**Sources:**
1. [Zeroheight MCP Help](https://help.zeroheight.com/hc/en-us/articles/39914754674843-Using-the-local-zeroheight-MCP-server) -- Setup guide
2. [Zeroheight MCP npm](https://www.npmjs.com/package/@zeroheight/mcp-server) -- npm package
3. [Zeroheight API Documentation](https://developers.zeroheight.com/) -- REST API docs
4. [Zeroheight MCP Announcement](https://zeroheight.com/whats-new/direct-ai-access-to-your-design-system-documentation/) -- Product announcement

---

### 1.10 Framer -- Interactive Prototyping, Web Design

**Status: EXISTING MCP (Official Server API + Community MCP)**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | Yes -- official Framer MCP plugin + community server |
| **API Available?** | Server API (Feb 2026), Plugin API |
| **MCP Feasibility** | N/A -- already exists |
| **Tiny Team Value** | **Medium** |

#### MCP Server Implementations

| Server | Type | Capabilities |
|--------|------|-------------|
| **Framer MCP Plugin** | Official (Marketplace) | Design automation, React code export, AI-assisted design updates via natural language. Commercial (advanced features paid). |
| **framer-plugin-mcp** (Sheshiyer) | Community (open-source) | Framer plugin creation and management with Web3 capabilities. Self-hosted. |

#### API Capabilities (Server API, Feb 2026)

- Programmatic access to Framer projects without opening the app.
- Update and publish projects from any server.
- Script-based automation of design workflows.

#### Integration Patterns for AI Agents

- **Prototype Generation**: Agent creates interactive prototypes from specifications.
- **React Export**: Agent converts Framer designs to production React code.
- **Design Updates**: Agent modifies existing Framer projects based on feedback.

**Sources:**
1. [Framer Server API Introduction](https://www.framer.com/developers/server-api-introduction) -- Official docs
2. [framer-plugin-mcp GitHub](https://github.com/Sheshiyer/framer-plugin-mcp) -- Community MCP
3. [Framer MCP Server LobeHub](https://lobehub.com/mcp/sheshiyer-framer-plugin-mcp) -- Listing

---

### 1.11 Penpot -- Open-Source Design Tool

**Status: EXISTING MCP (Official, Experimental)**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | Yes -- official Penpot MCP (experimental) + community servers |
| **API Available?** | Open Plugin API, REST API (self-hosted) |
| **MCP Feasibility** | N/A -- already exists |
| **Tiny Team Value** | **Medium** (High if team values open-source/self-hosting) |

#### MCP Server Implementations

| Server | Maintainer | Status |
|--------|-----------|--------|
| **penpot-mcp** | Penpot (official) | Experimental -- not yet beta. Active development. |
| **penpot-mcp** (montevive) | Community | Available on GitHub. |
| **penpot-mcp-server** (zcube) | Community | npm: `@zcubekr/penpot-mcp-server`. Connects AI assistants to Penpot. |

#### Key Differentiator: Design-as-Code

Penpot's design-expressed-as-code approach means designs can be programmatically created, edited, and analyzed at a granular level. This makes it architecturally superior for deep AI integration compared to tools where the design format is opaque.

#### MCP Capabilities

- Retrieve design data from Penpot projects.
- Modify and create design elements programmatically.
- Translate AI intent into API requests.
- Works with any MCP-enabled AI assistant.

#### Integration Patterns for AI Agents

- **Full Design Automation**: Agent creates entire wireframes and UI layouts from specifications.
- **Design-to-Code Bidirectional**: Agent reads designs as code, modifies them, and regenerates.
- **Self-Hosted Control**: Team controls both the design tool and the MCP server infrastructure.

**Sources:**
1. [Penpot MCP Server Page](https://penpot.app/penpot-mcp-server) -- Official page
2. [Penpot MCP GitHub](https://github.com/penpot/penpot-mcp) -- Official repository
3. [Smashing Magazine: Penpot MCP](https://www.smashingmagazine.com/2026/01/penpot-experimenting-mcp-servers-ai-powered-design-workflows/) -- January 2026 coverage

---

### 1.12 Whimsical -- Wireframing, Flowcharts

**Status: EXISTING MCP (Community)**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | Yes -- community implementation by Brock Reece |
| **API Available?** | Whimsical API (used by MCP server) |
| **MCP Feasibility** | N/A -- community MCP exists |
| **Tiny Team Value** | **Medium** |

#### MCP Server Capabilities

- Accepts Mermaid markup and creates Whimsical diagrams.
- Returns both live Whimsical diagram URL and base64-encoded image preview.
- Supports flowcharts and sequence diagrams (Mermaid-supported types).
- **Limitation**: Does not support mind maps or wireframes (only Mermaid-compatible diagram types).

#### Integration Patterns for AI Agents

- **Flowchart Generation**: Agent generates user flow diagrams from text descriptions.
- **Sequence Diagrams**: Agent creates interaction diagrams for API/system design.
- **Iterative Refinement**: Agent receives base64 preview, analyzes, and regenerates improved markup.

**Sources:**
1. [Whimsical MCP GitHub](https://github.com/BrockReece/whimsical-mcp-server) -- MIT-licensed
2. [Whimsical MCP PulseMCP](https://www.pulsemcp.com/servers/brockreece-whimsical) -- Listing

---

### 1.13 UserTesting -- Remote User Testing Platform

**Status: FEASIBLE MCP (Medium difficulty)**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | No |
| **API Available?** | Yes -- Results API (v2), Legacy API (v1). HTTPS + OAuth2 Bearer Token. |
| **MCP Feasibility** | Medium -- API exists, custom MCP adapter buildable |
| **Tiny Team Value** | **Medium** |

#### API Capabilities

- **Results API (v2)**: Access QXscores, session data, videos, transcripts.
- **Legacy API (v1)**: Basic data retrieval.
- Partner Authentication (Client ID + Secret) + OAuth2 Bearer Token.
- HTTPS required for all requests.

#### Integration Patterns (If MCP Were Built)

- **Test Results Retrieval**: Agent fetches QXscores and session transcripts for analysis.
- **Transcript Analysis**: Agent processes user testing transcripts to identify usability issues.
- **Cross-Study Synthesis**: Agent aggregates findings across multiple studies.

**Sources:**
1. [UserTesting APIs](https://developer.usertesting.com/) -- Developer portal

---

### 1.14 Optimal Workshop -- Information Architecture Testing

**Status: NOT FEASIBLE (No Public API)**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | No |
| **API Available?** | No public REST API documented |
| **MCP Feasibility** | Low -- no API to wrap |
| **Tiny Team Value** | **Low** (niche use case) |

Optimal Workshop provides tree testing and card sorting tools for information architecture. However, no public API has been identified for programmatic access to test results or study configuration. Without an API, building an MCP adapter would require browser automation, which is fragile and unreliable.

**Sources:**
1. [Optimal Workshop](https://www.optimalworkshop.com/) -- Product page (no API documentation found)

---

### 1.15 Lookback -- User Research Platform

**Status: NOT FEASIBLE (No Public API)**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | No |
| **API Available?** | No public REST API documented |
| **MCP Feasibility** | Low -- no API to wrap |
| **Tiny Team Value** | **Low** |

Lookback offers moderated and unmoderated user research sessions with screen, audio, and video capture. It integrates with User Interviews but has no documented public API for programmatic access. MCP adapter creation would require reverse-engineering or browser automation.

**Sources:**
1. [Lookback](https://www.lookback.com) -- Product page

---

### 1.16 Abstract -- Design Version Control

**Status: NOT FEASIBLE (Legacy Platform)**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | No |
| **API Available?** | Legacy API (limited, status uncertain) |
| **MCP Feasibility** | Low -- declining platform, Sketch-dependent |
| **Tiny Team Value** | **None** |

Abstract provides version control for Sketch and Adobe XD files. The platform appears to still be operational but is in maintenance mode. With Figma's built-in version history and branching, Abstract's value proposition has significantly diminished. No MCP server exists, and building one would serve a shrinking user base.

**Sources:**
1. [Abstract](https://www.goabstract.com/) -- Product page

---

### 1.17 Lottie/LottieFiles -- Animation

**Status: EXISTING MCP (Community)**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | Yes -- community MCP for LottieFiles |
| **API Available?** | LottieFiles API (search, retrieval) |
| **MCP Feasibility** | N/A -- community MCP exists |
| **Tiny Team Value** | **Medium** |

#### MCP Server Capabilities

- **Search animations**: Search LottieFiles library by keyword, tags, description.
- **Retrieve details**: Get metadata for specific animations.
- **Popular animations**: List currently trending animations.
- **Pagination**: Paginated search results.
- Install via Smithery: `npx -y smithery install mcp-server-lottiefiles --client claude`

#### Integration Patterns for AI Agents

- **Animation Discovery**: Agent searches for contextually appropriate animations based on UI requirements.
- **Asset Integration**: Agent retrieves Lottie JSON for embedding in React/Vue components.
- **Loading State Design**: Agent selects appropriate loading animations from the library.

**Sources:**
1. [LottieFiles MCP GitHub](https://github.com/junmer/mcp-server-lottiefiles) -- Repository
2. [LottieFiles MCP Market](https://mcpmarket.com/es/server/lottiefiles) -- Marketplace listing

---

### 1.18 Rive -- Animation Tool

**Status: EXISTING MCP (Official, Early Access)**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | Yes -- official Rive Editor MCP (Early Access) + docs MCP |
| **API Available?** | Editor API (via MCP), Runtime SDKs (React, Flutter, Unity) |
| **MCP Feasibility** | N/A -- official MCP exists |
| **Tiny Team Value** | **Medium** |

#### MCP Server Implementations

| Server | Type | Capabilities |
|--------|------|-------------|
| **Rive Editor MCP** | Official (Early Access) | Create/modify View Models, State Machines, Layouts, Shapes via natural language. Requires Early Access Mac desktop app. |
| **Rive Docs MCP** | Community | Access Rive documentation, runtime guides, editor features, tutorials. Search across web, mobile, game platforms. |
| **Rive MCP Server Core** | Community (npm) | Bridges AI assistants with Rive animations: discovery, code generation, integration. |

#### Limitations

- Editor MCP requires Early Access Mac desktop app (Windows planned).
- Full bidirectional control only via the desktop app MCP.

#### Integration Patterns for AI Agents

- **Interactive Animation Creation**: Agent creates complex state machines and animations via natural language.
- **Runtime Integration**: Agent generates framework-specific code (React, Flutter, Unity) for Rive animations.
- **Documentation Lookup**: Agent queries Rive docs for implementation guidance.

**Sources:**
1. [Rive MCP Integration](https://rive.app/docs/editor/mcp/integration) -- Official docs
2. [Rive x MCP Community Post](https://community.rive.app/c/announcements/rive-x-mcp-connect-rive-to-ai-tools) -- Announcement
3. [Rive MCP Server Core npm](https://www.npmjs.com/package/@rive-mcp/server-core) -- npm package

---

### 1.19 Principle -- Animation Prototyping

**Status: NOT FEASIBLE (No API)**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | No |
| **API Available?** | No public API. Mac-only desktop app. |
| **MCP Feasibility** | Low -- closed ecosystem, no extensibility |
| **Tiny Team Value** | **None** |

Principle is a macOS-only animation prototyping tool that uses state transitions between artboards. It integrates with Figma and Sketch for design import but provides no API, plugin system, or extensibility mechanism suitable for MCP adapter creation.

**Sources:**
1. [Principle](https://principleformac.com/) -- Product page

---

### 1.20 Axure -- Advanced Prototyping, Documentation

**Status: FEASIBLE MCP (Low priority)**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | No |
| **API Available?** | Legacy RP API (status uncertain -- may be deprecated) |
| **MCP Feasibility** | Low-Medium -- legacy API, uncertain support |
| **Tiny Team Value** | **Low** |

Axure RP is a prototyping and specification tool used primarily in enterprise settings. A "Legacy RP API" exists on axure.com, but its current status and capabilities are unclear. No MCP server exists. Building one would serve a declining user base in the context of Figma's dominance.

**Sources:**
1. [Axure Legacy RP API](https://www.axure.com/axure-rp-api) -- Legacy API reference

---

### 1.21 Balsamiq -- Low-Fidelity Wireframing

**Status: FEASIBLE MCP (Alternative exists: Frame0)**

| Dimension | Detail |
|-----------|--------|
| **MCP Server Exists?** | No direct Balsamiq MCP. **Frame0 MCP exists** as a Balsamiq-alternative with MCP support. |
| **API Available?** | Native API and developer docs available at balsamiq.com/docs |
| **MCP Feasibility** | Medium -- API exists; but Frame0 MCP is a better alternative |
| **Tiny Team Value** | **Medium** (for low-fi wireframing workflows) |

#### Alternative: Frame0 MCP Server

Frame0 is a modern Balsamiq alternative specifically designed for AI-powered wireframing. It has an MCP plugin that enables "vibe wireframing" -- creating and modifying wireframes by prompting.

#### Integration Patterns

- **AI Wireframing**: Use Frame0 MCP to generate low-fidelity wireframes from user stories or requirements.
- **Rapid Ideation**: Agent creates multiple wireframe variants from a single brief.

**Sources:**
1. [Frame0 MCP Glama](https://glama.ai/mcp/servers/@niklauslee/frame0-mcp-server) -- Frame0 MCP listing
2. [Balsamiq API Tracker](https://apitracker.io/a/balsamiq) -- API availability

---

### Summary Matrix

| # | Tool | MCP Status | API Available | MCP Feasibility | Tiny Team Value |
|---|------|-----------|---------------|-----------------|-----------------|
| 1 | **Figma** | EXISTING (Official + Community) | REST + Plugin | N/A | **Critical** |
| 2 | **Miro** | EXISTING (Official) | REST v2 | N/A | **Critical** |
| 3 | Sketch | EXISTING (Community) | JS Plugin + File | N/A | Low |
| 4 | Adobe XD | EXISTING (Community) | Plugin + File | N/A | Low |
| 5 | InVision | NOT FEASIBLE | Discontinued | N/A | None |
| 6 | Maze | No MCP | Limited integrations | Medium | **High** |
| 7 | **Hotjar** | EXISTING (Third-party) | REST (limited) | N/A | **High** |
| 8 | **Storybook** | EXISTING (Official) | N/A (dev tool) | N/A | **Critical** |
| 9 | **Zeroheight** | EXISTING (Official) | REST API | N/A | **High** |
| 10 | Framer | EXISTING (Official) | Server API | N/A | Medium |
| 11 | Penpot | EXISTING (Official, Experimental) | Plugin + REST | N/A | Medium |
| 12 | Whimsical | EXISTING (Community) | API | N/A | Medium |
| 13 | UserTesting | No MCP | REST API v2 | Medium | Medium |
| 14 | Optimal Workshop | No MCP | No public API | Low | Low |
| 15 | Lookback | No MCP | No public API | Low | Low |
| 16 | Abstract | No MCP | Legacy API | Low | None |
| 17 | LottieFiles | EXISTING (Community) | LottieFiles API | N/A | Medium |
| 18 | Rive | EXISTING (Official, Early Access) | Editor API | N/A | Medium |
| 19 | Principle | No MCP | No API | Low | None |
| 20 | Axure | No MCP | Legacy API | Low-Medium | Low |
| -- | Balsamiq | No MCP (Frame0 alternative) | Native API | Medium | Medium |

---

## L2: Integration Architecture

### Tier Model for MCP Integration

#### Tier 1: Deploy Now (Existing, Production-Ready MCP Servers)

These have official or mature community MCP servers ready for immediate use in a Tiny Team setup.

| Tool | Server | Install Method | Use in UX Workflow |
|------|--------|---------------|-------------------|
| **Figma** | Official Dev Mode MCP | Figma settings | Design-to-code, token extraction, asset export |
| **Figma** | Framelink MCP | npm/npx | Simplified layout data for AI |
| **Figma** | Cursor Talk to Figma | npm + Figma plugin | Bidirectional design manipulation |
| **Miro** | Official Miro MCP | Miro admin setup | Board reading, diagram generation, PRD extraction |
| **Storybook** | @storybook/addon-mcp | npm addon | Component discovery, story generation |
| **Zeroheight** | @zeroheight/mcp-server | npm | Design system docs, token resolution |
| **Hotjar** | Zapier/Pipedream MCP | Zapier/Pipedream config | Survey response analysis |

**Effort to integrate: Low (hours to days)**

#### Tier 2: Build Adapters (API Available, MCP Buildable)

These tools have APIs but no MCP server. Custom MCP adapters can be built using the MCP SDK.

| Tool | API Type | Adapter Complexity | Priority |
|------|----------|-------------------|----------|
| **Maze** | REST (limited) + Figma integration | Medium | High -- user testing data is a major gap |
| **UserTesting** | REST API v2 (OAuth2) | Medium | Medium -- useful for teams with UserTesting subscriptions |
| **Framer** | Server API (Feb 2026) | Low | Low -- Figma covers most use cases |

**Effort to build: Days to weeks per adapter**

#### Tier 3: Future / Watch List

These tools either lack APIs, are declining, or have niche use cases not worth immediate investment.

| Tool | Reason | Watch For |
|------|--------|-----------|
| Penpot | Experimental MCP -- watch for beta | Beta release announcement |
| Rive | Early Access MCP -- watch for GA | Windows support, GA release |
| Maze | No public REST API yet | Public API announcement |
| Optimal Workshop | No API | API launch |
| Lookback | No API | API launch |
| Frame0 | Balsamiq alternative with MCP | Maturity and adoption |

#### Tier 4: Deprecated / Skip

| Tool | Reason |
|------|--------|
| InVision | Shut down (Dec 2024) |
| Abstract | Declining, Sketch-dependent |
| Principle | No API, no extensibility |
| Adobe XD | Declining investment by Adobe |
| Axure | Legacy API, enterprise-only niche |

### Recommended Integration Priority for /user-experience Skill

For the Jerry `/user-experience` skill, integrations should be prioritized by the UX workflow phase they enable:

| Priority | Phase | Tool(s) | MCP Integration | Workflow Enabled |
|----------|-------|---------|-----------------|-----------------|
| **P1** | Design | Figma | Tier 1 (existing) | AI reads designs, generates code, extracts tokens |
| **P2** | Design System | Storybook + Zeroheight | Tier 1 (existing) | AI enforces design system compliance |
| **P3** | Collaboration | Miro | Tier 1 (existing) | AI reads PRDs, journey maps, generates diagrams |
| **P4** | Analytics | Hotjar | Tier 1 (existing, via Zapier) | AI analyzes user behavior data |
| **P5** | User Testing | Maze | Tier 2 (build adapter) | AI analyzes usability test results |
| **P6** | Animation | LottieFiles + Rive | Tier 1/3 (mixed) | AI discovers and integrates animations |
| **P7** | Wireframing | Whimsical / Frame0 | Tier 1 (community) | AI generates flowcharts and wireframes |

### How MCP Integrations Enable Tiny Team UX Workflows

#### Workflow 1: AI-Assisted Design-to-Code Pipeline

```
[User creates design in Figma]
    |
    v
[Figma MCP] --> Agent reads layout, tokens, component specs
    |
    v
[Zeroheight MCP] --> Agent checks design system guidelines
    |
    v
[Storybook MCP] --> Agent discovers existing components
    |
    v
Agent generates production code matching design + design system + existing components
```

**Impact**: Eliminates the "design handoff" bottleneck. A 2-person team (designer + developer) can ship UI 2-3x faster because the AI handles the translation layer.

#### Workflow 2: AI-Assisted User Research Synthesis

```
[Team runs usability test in Maze]
    |
    v
[Maze integration / manual export] --> Agent analyzes test metrics
    |
    v
[Hotjar MCP] --> Agent correlates with behavioral analytics
    |
    v
[Miro MCP] --> Agent updates journey map with findings
    |
    v
Agent generates UX improvement recommendations document
```

**Impact**: Replaces the need for a dedicated UX researcher. AI synthesizes quantitative (Maze metrics, Hotjar heatmaps) and qualitative (survey responses) data into actionable recommendations.

#### Workflow 3: AI-Assisted Design System Management

```
[Developer creates new component]
    |
    v
[Storybook MCP] --> Agent generates stories + documentation
    |
    v
[Zeroheight MCP] --> Agent checks naming + usage guidelines
    |
    v
[Figma MCP] --> Agent verifies component matches Figma design
    |
    v
Agent flags inconsistencies and auto-generates design system documentation updates
```

**Impact**: Design system maintenance -- normally a full-time role -- becomes an automated workflow. The AI keeps Storybook, Zeroheight, and Figma in sync.

### Technical Patterns: How Agents Interact with MCP Servers

#### Pattern 1: Read-Analyze-Recommend (Most MCP Servers)

Most design MCP servers are read-only. The agent reads design data, analyzes it against criteria, and produces recommendations or generated code.

```
Agent --> [MCP Tool Call: get_design_context] --> Figma MCP Server --> Figma API
Agent <-- Structured design data (layout, tokens, components)
Agent --> [Internal reasoning: generate code matching design]
Agent --> [Write tool: create component file]
```

#### Pattern 2: Read-Write Bidirectional (Cursor Talk to Figma, Penpot)

A few MCP servers support creating and modifying designs. This enables full AI-driven design workflows.

```
Agent --> [MCP Tool Call: create_rectangle] --> WebSocket --> Figma Plugin
Agent <-- Confirmation + element ID
Agent --> [MCP Tool Call: set_fill_color] --> WebSocket --> Figma Plugin
Agent <-- Updated element data
```

#### Pattern 3: Bridge MCP (Zapier/Pipedream for Hotjar, etc.)

Third-party platforms like Zapier wrap existing APIs as MCP tools, providing MCP access without custom server development.

```
Agent --> [MCP Tool Call: hotjar_get_survey_responses] --> Zapier MCP --> Hotjar API
Agent <-- Survey response JSON
```

### Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| MCP server API changes break integration | Medium | High | Pin MCP server versions; monitor changelogs |
| Figma API rate limits during heavy AI usage | Medium | Medium | Cache design data locally; use incremental reads |
| Third-party MCP servers (Zapier) have latency | High | Low | Pre-fetch data at workflow start, not per-query |
| Penpot/Rive MCP servers are experimental | High | Low | Use as supplementary, not primary tools |
| User research tools lack APIs | High | Medium | Advocate for API access; use manual export + AI analysis |
| MCP ecosystem fragmentation (multiple servers per tool) | Medium | Low | Standardize on official servers when available |

### Future Evolution Path

1. **Near-term (0-3 months)**: Deploy Tier 1 servers (Figma, Miro, Storybook, Zeroheight, Hotjar). Configure in Jerry's MCP settings.
2. **Short-term (3-6 months)**: Build Maze MCP adapter when/if public API launches. Monitor Penpot and Rive MCP for beta/GA.
3. **Medium-term (6-12 months)**: Evaluate whether Figma's bidirectional MCP (Cursor Talk to Figma) is stable enough for production UX automation. Build UserTesting adapter if team adopts the platform.
4. **Long-term (12+ months)**: As user research tools release APIs, build adapters. Evaluate whether Penpot can replace Figma for teams wanting open-source control.

---

## References

### Official Documentation

1. [Figma MCP Server Guide](https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server) -- Official setup and capabilities
2. [Figma MCP Blog Announcement](https://www.figma.com/blog/introducing-figma-mcp-server/) -- Strategic context
3. [Figma Developer Docs - MCP](https://developers.figma.com/docs/figma-mcp-server/) -- Technical reference
4. [Figma REST API](https://developers.figma.com/docs/rest-api/) -- API endpoints and capabilities
5. [Miro MCP Developer Docs](https://developers.miro.com/docs/miro-mcp) -- Official MCP documentation
6. [Miro MCP Help Center](https://help.miro.com/hc/en-us/articles/31624028247058-Miro-MCP-Server-overview) -- Setup guide
7. [Miro MCP Blog](https://miro.com/blog/bringing-organizational-context-to-ai-with-miro-mcp/) -- Strategic announcement
8. [Storybook Addon MCP](https://storybook.js.org/addons/@storybook/addon-mcp) -- Official addon
9. [Storybook MCP GitHub](https://github.com/storybookjs/mcp) -- Official repository
10. [Zeroheight MCP Local Setup](https://help.zeroheight.com/hc/en-us/articles/39914754674843-Using-the-local-zeroheight-MCP-server) -- Setup guide
11. [Zeroheight MCP Remote Setup](https://help.zeroheight.com/hc/en-us/articles/43780251357979-Using-the-remote-zeroheight-MCP-server) -- Remote configuration
12. [Zeroheight API Documentation](https://developers.zeroheight.com/) -- REST API reference
13. [Zeroheight MCP npm](https://www.npmjs.com/package/@zeroheight/mcp-server) -- Package (v2.1.1)
14. [Framer Server API](https://www.framer.com/developers/server-api-introduction) -- Official API docs
15. [Penpot MCP Official](https://penpot.app/penpot-mcp-server) -- Official page
16. [Penpot MCP GitHub](https://github.com/penpot/penpot-mcp) -- Official repository
17. [Rive MCP Integration](https://rive.app/docs/editor/mcp/integration) -- Official docs
18. [Rive MCP Community](https://community.rive.app/c/announcements/rive-x-mcp-connect-rive-to-ai-tools) -- Announcement
19. [Hotjar API Reference](https://help.hotjar.com/hc/en-us/articles/36820005914001-Hotjar-API-Reference) -- API documentation
20. [Hotjar Events API](https://help.hotjar.com/hc/en-us/articles/36819965075473-Events-API-Reference) -- Events reference
21. [UserTesting APIs](https://developer.usertesting.com/) -- Developer portal
22. [Adobe Express Developer MCP](https://developer.adobe.com/express/add-ons/docs/guides/getting_started/local_development/mcp_server/) -- Official Adobe MCP
23. [Axure Legacy RP API](https://www.axure.com/axure-rp-api) -- Legacy API reference

### Community MCP Servers

24. [Figma-Context-MCP (Framelink)](https://github.com/GLips/Figma-Context-MCP) -- Community Figma MCP
25. [Cursor Talk to Figma](https://github.com/grab/cursor-talk-to-figma-mcp) -- Bidirectional Figma MCP by Grab
26. [Sketch-Context-MCP](https://github.com/jshmllr/sketch-context-mcp) -- Sketch file parser MCP
27. [Adobe XD MCP](https://github.com/dekdee/adobe-xd-mcp) -- Community Adobe XD MCP
28. [Adobe Creative Suite MCP](https://github.com/matrayu/adobe-mcp) -- Unified Adobe MCP
29. [Whimsical MCP](https://github.com/BrockReece/whimsical-mcp-server) -- Mermaid-to-Whimsical MCP
30. [LottieFiles MCP](https://github.com/junmer/mcp-server-lottiefiles) -- Animation search MCP
31. [Rive MCP Server Core](https://www.npmjs.com/package/@rive-mcp/server-core) -- Community Rive bridge
32. [Rive Docs MCP](https://github.com/StormXX/rive-docs-mcp) -- Documentation MCP
33. [Penpot MCP (montevive)](https://github.com/montevive/penpot-mcp) -- Community implementation
34. [Penpot MCP Server (zcube)](https://github.com/zcube/penpot-mcp-server) -- Community implementation
35. [framer-plugin-mcp](https://github.com/Sheshiyer/framer-plugin-mcp) -- Community Framer MCP
36. [Frame0 MCP](https://glama.ai/mcp/servers/@niklauslee/frame0-mcp-server) -- Balsamiq-alternative wireframing

### Third-Party MCP Bridges

37. [Hotjar MCP via Zapier](https://zapier.com/mcp/hotjar) -- Zapier MCP bridge
38. [Hotjar MCP via Pipedream](https://mcp.pipedream.com/app/hotjar) -- Pipedream MCP bridge

### Industry Coverage and Analysis

39. [14 MCP Servers for UI/UX Engineers - Snyk](https://snyk.io/articles/14-mcp-servers-for-ui-ux-engineers/) -- Ecosystem overview
40. [Best MCP Servers for Designers - mcpevals.io](https://www.mcpevals.io/blog/best-mcp-servers-for-designers) -- Design-focused evaluation
41. [Design Tools MCP Servers - MCP Market](https://mcpmarket.com/categories/design-tools) -- Marketplace category
42. [MCP Stack for UI/UX Designers - Skywork](https://skywork.ai/skypage/en/A-Technical-Deep-Dive-into-MCP-Stack-for-UI-UX-Designers:-The-End-to-End-AI-Workflow/1971471535930667008) -- End-to-end workflow analysis
43. [7 Best UI Design MCP Servers - Medium](https://medium.com/@joe.njenga/7-best-ui-design-mcp-servers-that-will-10x-your-design-workflow-e8f3fe22c357) -- Curated list
44. [Figma Make + Zeroheight Connectors](https://www.cmswire.com/digital-experience/figma-make-adds-custom-model-context-protocol-6-new-connectors/) -- Feb 2026 Figma Make expansion
45. [Penpot MCP - Smashing Magazine](https://www.smashingmagazine.com/2026/01/penpot-experimenting-mcp-servers-ai-powered-design-workflows/) -- Jan 2026 coverage
46. [InVision Shutdown - LogRocket](https://blog.logrocket.com/ux-design/invision-shutting-down/) -- Platform discontinuation
47. [MCP Architecture Overview](https://modelcontextprotocol.io/docs/learn/architecture) -- Protocol specification
48. [Anthropic MCP Introduction](https://www.anthropic.com/news/model-context-protocol) -- Protocol launch announcement

---

## Research Methodology

**Search strategy**: Each of the 20 tools was individually searched with queries targeting "[tool name] MCP server", "[tool name] API", and "[tool name] model context protocol". Broader ecosystem searches were conducted for "MCP servers design tools" and "MCP servers UI/UX". Results were cross-referenced across multiple search engines and MCP directories (MCP Market, LobeHub, Awesome MCP Servers, PulseMCP).

**Source hierarchy**: Official documentation (Figma, Miro, Storybook, Zeroheight, Rive, Penpot) was prioritized as primary sources. GitHub repositories provided technical capability verification. Industry analysis articles (Snyk, Smashing Magazine, Skywork) provided contextual validation.

**Limitations**:
- API capability details for Maze and Lookback were not found in public documentation. These tools may have private/partner APIs not discoverable via web search.
- Some community MCP servers may be unmaintained or experimental. Maintenance status was not systematically verified for all 36+ MCP implementations listed.
- Pricing details for MCP servers (especially Framer's commercial MCP plugin) were not systematically captured.

---

*Research conducted: 2026-03-02*
*Agent: ps-researcher*
*Project: PROJ-020-feature-enhancements*
