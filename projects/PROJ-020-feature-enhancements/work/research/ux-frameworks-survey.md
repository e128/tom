# UX Frameworks and Methodologies: Comprehensive Survey

> **PS ID:** proj-020 | **Topic:** UX Design Frameworks Survey | **Date:** 2026-03-02
> **Agent:** ps-researcher | **Confidence:** 0.87 (High -- broad coverage from multiple credible sources with some depth limitations on newer/emerging frameworks)

## Document Sections

| Section | Purpose |
|---------|---------|
| [L0 -- Executive Summary](#l0----executive-summary) | Plain-language overview and key takeaways |
| [L1 -- Framework Catalog](#l1----framework-catalog) | Structured entries for all 35 frameworks |
| [Category 1: Process-Oriented](#category-1-process-oriented-frameworks) | End-to-end design process methodologies |
| [Category 2: Evaluation and Metrics](#category-2-evaluation-and-metrics-frameworks) | Measurement and assessment frameworks |
| [Category 3: Strategic and Business](#category-3-strategic-and-business-frameworks) | Business-aligned UX strategy |
| [Category 4: Behavioral and Psychological](#category-4-behavioral-and-psychological-frameworks) | Human behavior and motivation |
| [Category 5: Component and System Architecture](#category-5-component-and-system-architecture-frameworks) | UI structure and design systems |
| [Category 6: Accessibility and Ethics](#category-6-accessibility-and-ethics-frameworks) | Inclusive, ethical, and value-driven design |
| [Category 7: Operational](#category-7-operational-frameworks) | Design team operations and scaling |
| [Category 8: Emerging and AI-Native](#category-8-emerging-and-ai-native-frameworks) | Newer frameworks addressing AI and complexity |
| [L2 -- Deep Analysis](#l2----deep-analysis) | Overlap mapping, evolution, AI readiness, gaps |
| [Methodology](#methodology) | Research approach and source assessment |
| [References](#references) | Full citation list |

---

## L0 -- Executive Summary

This research surveyed and cataloged **35 UX design frameworks and methodologies**, spanning process-oriented approaches, evaluation methods, strategic frameworks, behavioral models, component architectures, accessibility/ethics standards, operational practices, and emerging AI-native paradigms.

**What was researched and why it matters:**
UX frameworks are structured approaches that guide how products are designed, tested, and improved for human use. Think of them as "playbooks" for making software that people actually enjoy using. This survey catalogs the full landscape so that a tiny team (2-3 people augmented by AI) can select the right combination of frameworks for their specific needs rather than defaulting to one-size-fits-all approaches.

**Key findings in plain language:**
- The UX framework landscape is **mature and well-established** -- most major frameworks date from the 1990s-2010s, with refinements rather than replacements emerging since
- There is a clear **convergence around human-centered, iterative processes** -- despite different names and structures, nearly all frameworks share empathy-research-prototype-test cycles
- The biggest **gap in the landscape is AI-native design** -- existing frameworks were built for human-only teams and struggle with AI-augmented workflows, multimodal interfaces, and agent-based UX
- For AI-augmented tiny teams, **lightweight process frameworks** (Design Sprint, Lean UX, Rapid Contextual Design) combined with **evaluation heuristics** (Nielsen's 10, HEART) offer the best return on investment

**Top 5 takeaways:**
1. **No single framework covers everything.** The most effective approach combines a process framework (how to work) + an evaluation framework (how to measure) + a structural framework (how to organize components).
2. **The "tiny teams" trend demands framework composability.** Frameworks that can be adopted partially and incrementally are far more valuable than monolithic methodologies requiring dedicated UX departments.
3. **AI augmentation readiness varies dramatically.** Behavioral/psychological frameworks (Hook Model, Fogg Behavior Model) translate well to AI-assisted design. Heavy ethnographic methods (Contextual Design) are harder to automate.
4. **Ethics and accessibility are no longer optional add-ons.** The REFLECT framework, Microsoft Inclusive Design, and Value Sensitive Design represent a growing movement to embed ethics into methodology rather than treat it as a compliance checkbox.
5. **The strongest candidates for Jerry sub-skills are frameworks with clear, repeatable steps** -- Design Sprint (5 days), Nielsen's Heuristics (10 checklist items), HEART (5 metrics), and Double Diamond (4 phases) all have high composability scores.

---

## L1 -- Framework Catalog

### Category 1: Process-Oriented Frameworks

These frameworks define end-to-end design processes with phases, activities, and deliverables.

---

#### 1. User-Centered Design (UCD)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Don Norman; coined ~1986, formalized in ISO 9241-210 (2010) |
| **Core Principles** | (1) Focus on users and tasks early, (2) Empirical measurement of usage, (3) Iterative design, (4) Multidisciplinary team, (5) Active user involvement |
| **Strengths** | ISO-standardized; universally recognized; adaptable to any project scale; strong research foundation |
| **Weaknesses** | Can be slow and expensive when fully applied; user involvement sometimes tokenistic; risk of "design by committee" |
| **Tiny Team Applicability** | **Medium-High** -- Core principles apply well; the process overhead can be trimmed. AI can accelerate user research phases (automated surveys, sentiment analysis). |
| **Maturity Level** | Mature |
| **Community Adoption** | Very High |
| **Jerry Sub-Skill Composability** | **Medium** -- Too broad to be a single skill; better decomposed into specific UCD activities (contextual inquiry, usability testing) as sub-methods |

**Source:** [ISO 9241-210](https://www.iso.org/standard/77520.html); [NN/g UCD Articles](https://www.nngroup.com/articles/usability-101-introduction-to-usability/)

---

#### 2. Design Thinking (IDEO/Stanford d.school)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Tim Brown / IDEO; Stanford d.school; popularized 2000s-2010s. Roots in Herbert Simon's "Sciences of the Artificial" (1969) |
| **Core Principles** | (1) Empathize, (2) Define, (3) Ideate, (4) Prototype, (5) Test |
| **Strengths** | Highly accessible; strong workshop format; promotes cross-functional collaboration; well-documented with extensive toolkits (IDEO Field Guide has 57 methods) |
| **Weaknesses** | Can be superficial when applied as a checklist; criticized for lacking rigor vs. academic HCI methods; sometimes treated as a silver bullet; can become "design thinking theater" |
| **Tiny Team Applicability** | **High** -- Workshop-based, works well with small groups. AI can assist with empathy mapping, rapid prototyping, and pattern synthesis from user data. |
| **Maturity Level** | Mature |
| **Community Adoption** | Very High |
| **Jerry Sub-Skill Composability** | **High** -- Clear 5-phase structure maps naturally to a guided methodology skill with phase gates |

**Source:** [IDEO Design Thinking](https://designthinking.ideo.com/); [IDEO.org Field Guide](https://www.ideo.com/journal/design-kit-the-human-centered-design-toolkit); [IxDF Design Thinking Overview](https://ixdf.org/literature/article/design-thinking-a-quick-overview)

---

#### 3. Lean UX

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Jeff Gothelf & Josh Seiden; book published 2013 (2nd ed. 2016, 3rd ed. 2021). Built on Lean Startup (Eric Ries) and Agile principles |
| **Core Principles** | (1) Outcomes over deliverables, (2) Build-Measure-Learn cycle, (3) Hypothesis-driven design, (4) Minimum Viable Products (MVPs), (5) Cross-functional collaboration |
| **Strengths** | Lightweight; integrates with Agile sprints; fast validation cycles; reduces wasted design documentation; data-driven decision making |
| **Weaknesses** | Can undervalue design craft and documentation; may skip deep user research in pursuit of speed; not ideal for highly regulated domains; hypothesis framing requires experience |
| **Tiny Team Applicability** | **Very High** -- Explicitly designed for small, cross-functional teams. AI augmentation fits naturally into hypothesis generation, rapid A/B testing, and analytics. |
| **Maturity Level** | Established |
| **Community Adoption** | High |
| **Jerry Sub-Skill Composability** | **High** -- Hypothesis template + experiment tracking maps well to a structured skill with clear inputs/outputs |

**Source:** [Lean UX Book](https://www.oreilly.com/library/view/lean-ux-3rd/9781098116293/); [Maze Lean UX Overview](https://maze.co/collections/ux-ui-design/ux-design-frameworks/)

---

#### 4. Agile UX

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Community-evolved practice, ~2006-2010. Key voices: Jeff Patton, Desiree Sy, Lynn Miller. Integrates UX design into Agile Scrum/Kanban workflows |
| **Core Principles** | (1) UX work in sprints alongside development, (2) Dual-track delivery (discovery + delivery), (3) Rapid prototype testing, (4) Cross-functional collaboration, (5) Just-enough documentation |
| **Strengths** | Aligns UX with engineering cadence; reduces handoff friction; promotes continuous user feedback; practical for product teams |
| **Weaknesses** | Sprint boundaries can fragment UX work; "one sprint ahead" pattern can feel rushed; difficult to do deep research within sprint constraints; UX debt accumulates |
| **Tiny Team Applicability** | **High** -- Small teams often already work in Agile; UX integration is natural. AI can pre-process user feedback between sprints. |
| **Maturity Level** | Established |
| **Community Adoption** | High |
| **Jerry Sub-Skill Composability** | **Medium** -- More of an integration pattern than a standalone methodology; works best as guidance within an existing sprint workflow |

**Source:** [UX Playbook Agile UX](https://uxplaybook.org/articles/5-fundamental-ux-design-frameworks-2026); [Maze UX Frameworks](https://maze.co/collections/ux-ui-design/ux-design-frameworks/)

---

#### 5. Double Diamond (UK Design Council)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | UK Design Council, 2004 (revised 2019 with systemic design additions) |
| **Core Principles** | (1) Discover -- diverge to understand the problem, (2) Define -- converge to frame the problem, (3) Develop -- diverge to generate solutions, (4) Deliver -- converge to implement. Underpinned by divergent/convergent thinking |
| **Strengths** | Visually intuitive; widely recognized; separates problem space from solution space; updated 2019 version adds systemic design principles |
| **Weaknesses** | Can be too abstract for practical guidance; doesn't specify methods within each diamond; may oversimplify messy real-world projects; linear representation can mislead |
| **Tiny Team Applicability** | **High** -- Simple mental model helps small teams stay oriented. The four phases can be compressed for faster cycles. AI can accelerate the Discover/Define phases through automated research synthesis. |
| **Maturity Level** | Mature |
| **Community Adoption** | Very High |
| **Jerry Sub-Skill Composability** | **High** -- Four clear phases with diverge/converge logic map to a structured skill with phase gates and criteria |

**Source:** [Design Council Framework for Innovation](https://www.designcouncil.org.uk/our-resources/framework-for-innovation/); [Design Council Systemic Design Framework](https://www.designcouncil.org.uk/our-resources/systemic-design-framework/)

---

#### 6. Design Sprint (Google Ventures)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Jake Knapp at Google (2010); refined at Google Ventures (2012); published as "Sprint" book (2016). Co-developed with Braden Kowitz, Michael Margolis, John Zeratsky, Daniel Burka |
| **Core Principles** | (1) Time-boxed 5-day process, (2) Map the problem (Monday), (3) Sketch solutions (Tuesday), (4) Decide (Wednesday), (5) Prototype (Thursday), (6) Test with 5 users (Friday) |
| **Strengths** | Extremely time-efficient; forces decisions; produces testable prototypes fast; works for startups and enterprises alike; proven at Slack, Airbnb, LEGO, Smithsonian, governments |
| **Weaknesses** | Requires full team dedication for a week; not suitable for all problem types; can skip deep research; one-week scope limits complex problem exploration |
| **Tiny Team Applicability** | **Very High** -- Designed for small teams. The 5-day structure prevents scope creep. AI can accelerate sketching, prototyping, and user testing analysis. |
| **Maturity Level** | Established |
| **Community Adoption** | Very High |
| **Jerry Sub-Skill Composability** | **Very High** -- Highly structured, time-boxed, with clear daily deliverables. Ideal as a guided skill with checklist gates per day. |

**Source:** [GV Sprint](https://www.gv.com/sprint/); [Sprint Book](https://www.thesprintbook.com/); [Design Sprint Kit](https://designsprintkit.withgoogle.com/)

---

#### 7. Goal-Directed Design (Alan Cooper)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Alan Cooper; first described in "About Face" (1995); refined through Cooper consulting practice. Kim Goodwin further developed the methodology |
| **Core Principles** | (1) Focus on user goals, not tasks, (2) Personas as primary design tool, (3) Separate design from programming, (4) Design before code, (5) Balance user, business, and engineering goals |
| **Strengths** | Persona methodology became industry standard; clear distinction between goals and tasks; prevents feature-driven design; produces coherent interaction models |
| **Weaknesses** | Heavy upfront research investment; persona creation can be time-consuming; "design before code" conflicts with Agile; personas can become stale or fictional |
| **Tiny Team Applicability** | **Medium** -- Persona creation is valuable but the full process is heavyweight. AI can dramatically accelerate persona synthesis from user data. |
| **Maturity Level** | Mature |
| **Community Adoption** | High |
| **Jerry Sub-Skill Composability** | **Medium** -- Persona creation methodology could be extracted as a standalone skill; the full process is too heavyweight |

**Source:** [Dubberly on Cooper](https://www.dubberly.com/articles/alan-cooper-and-the-goal-directed-design-process.html); [Cooper Journal](https://www.cooper.com/journal/2014/04/inside-goal-directed-design-a-two-part-conversation-with-alan-cooper/)

---

#### 8. Contextual Design (Holtzblatt & Beyer)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Karen Holtzblatt & Hugh Beyer; invented 1988; books in 1997, 2004 (Rapid CD), 2016 (Design for Life). Holtzblatt developed Contextual Inquiry field technique |
| **Core Principles** | (1) Go to the user's environment, (2) Contextual Inquiry interviews, (3) Work models (flow, sequence, artifact, cultural, physical), (4) Affinity diagramming, (5) Cross-functional interpretation sessions |
| **Strengths** | Deep ethnographic understanding; rigorous data collection; surfaces unconscious behaviors; team-based analysis; well-documented methodology |
| **Weaknesses** | Very labor-intensive; expensive field research; requires trained facilitators; can be slow for fast-paced product development; "Rapid CD" partially addresses this |
| **Tiny Team Applicability** | **Low-Medium** -- Full Contextual Design is too heavy for 2-3 people. Rapid Contextual Design (2004 adaptation) works with as few as 2 people in a few weeks. AI could help with interpretation session synthesis. |
| **Maturity Level** | Mature |
| **Community Adoption** | Medium |
| **Jerry Sub-Skill Composability** | **Low** -- Too ethnographic and field-dependent. Contextual Inquiry interview technique could be extracted as a method template. |

**Source:** [Contextual Design Wikipedia](https://en.wikipedia.org/wiki/Contextual_design); [Rapid Contextual Design (Holtzblatt et al. 2005)](https://www.sciencedirect.com/book/9780123540515/rapid-contextual-design)

---

#### 9. IBM Enterprise Design Thinking

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | IBM Design team, ~2013-2016. Built on traditional Design Thinking with enterprise-scale additions |
| **Core Principles** | (1) Observe-Reflect-Make loop, (2) Hills (user outcome-based success criteria), (3) Playbacks (storytelling checkpoints), (4) Sponsor Users (real users embedded in project), (5) Diverse empowered teams |
| **Strengths** | Scales Design Thinking to large organizations; Hills provide measurable goals; Playbacks create alignment; Sponsor Users ground decisions in reality; free online training and certification |
| **Weaknesses** | Enterprise-focused -- some overhead for tiny teams; IBM-branded training ecosystem; Hills methodology takes practice; may feel bureaucratic for startups |
| **Tiny Team Applicability** | **Medium** -- The Hills/Playbacks/Sponsor Users triad is useful at any scale. The enterprise coordination overhead is unnecessary for tiny teams but core ideas transfer well. |
| **Maturity Level** | Established |
| **Community Adoption** | High |
| **Jerry Sub-Skill Composability** | **Medium** -- Hills methodology could be extracted as a goal-setting method. The full framework is somewhat monolithic. |

**Source:** [IBM Enterprise Design Thinking](https://www.ibm.com/design/thinking/page/framework); [IBM Design Approach](https://www.ibm.com/design/approach/design-thinking/)

---

#### 10. Participatory Design / Co-Design

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Scandinavian tradition, 1970s. Rooted in workplace democracy movements in Denmark, Norway, Sweden. Key figures: Pelle Ehn, Susanne Bodker |
| **Core Principles** | (1) Users as equal collaborators (not just subjects), (2) Democratic design process, (3) Mutual learning between designers and users, (4) Workshop-based co-creation, (5) Include all stakeholders, not just end users |
| **Strengths** | Deep user empowerment; surfaces tacit knowledge; builds stakeholder buy-in; strong ethical foundation; applicable across physical and digital design |
| **Weaknesses** | Resource-intensive facilitation; can slow decision-making; power dynamics hard to manage; consensus-seeking can dilute innovation; logistically complex to assemble diverse participants |
| **Tiny Team Applicability** | **Medium** -- Co-design workshops work at small scale but require participant recruitment effort. AI can simulate stakeholder perspectives or help synthesize workshop outputs. |
| **Maturity Level** | Mature |
| **Community Adoption** | Medium |
| **Jerry Sub-Skill Composability** | **Low-Medium** -- Workshop facilitation guides could be templated, but the core value is in live human collaboration |

**Source:** [Participatory Design Wikipedia](https://en.wikipedia.org/wiki/Participatory_design); [Mural Co-Design Guide](https://www.mural.co/blog/co-design-method); [IxDF Participatory Design](https://ixdf.org/literature/topics/participatory-design)

---

### Category 2: Evaluation and Metrics Frameworks

These frameworks provide methods for measuring, evaluating, and assessing UX quality.

---

#### 11. Nielsen's 10 Usability Heuristics

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Jakob Nielsen & Rolf Molich (1990); refined by Nielsen in 1994 based on factor analysis of 249 usability problems |
| **Core Principles** | (1) Visibility of system status, (2) Match between system and real world, (3) User control and freedom, (4) Consistency and standards, (5) Error prevention, (6) Recognition over recall, (7) Flexibility and efficiency, (8) Aesthetic and minimalist design, (9) Help users recover from errors, (10) Help and documentation |
| **Strengths** | Universal applicability (web, mobile, desktop, emerging interfaces); 30+ years of validation; fast and inexpensive to apply; no user recruitment needed; well-understood by the industry |
| **Weaknesses** | Requires expert evaluators for quality results; cannot replace user testing; may miss context-specific issues; multiple evaluators needed for coverage; can produce false positives |
| **Tiny Team Applicability** | **Very High** -- A single person can run a heuristic evaluation in hours. AI can systematically evaluate interfaces against each heuristic. |
| **Maturity Level** | Mature |
| **Community Adoption** | Very High |
| **Jerry Sub-Skill Composability** | **Very High** -- 10 discrete, well-defined heuristics map perfectly to a checklist-based evaluation skill with scoring per heuristic |

**Source:** [NN/g 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/); [NN/g Heuristic Evaluation Method](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/)

---

#### 12. HEART Framework (Google)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Kerry Rodden, Hilary Hutchinson, Xin Fu at Google; published 2010 at CHI conference |
| **Core Principles** | (1) Happiness -- user satisfaction/attitudes, (2) Engagement -- depth/frequency of use, (3) Adoption -- new user acquisition, (4) Retention -- returning users, (5) Task Success -- efficiency/effectiveness/error rates. Uses Goals-Signals-Metrics (GSM) model |
| **Strengths** | Balances micro and macro metrics; combines behavioral and attitudinal measurement; GSM model makes metrics actionable; widely adopted at Google and beyond |
| **Weaknesses** | Requires analytics infrastructure; not all dimensions relevant for all products; can be overwhelming with too many metrics; attitudinal metrics (Happiness) harder to automate |
| **Tiny Team Applicability** | **High** -- Focused metrics prevent measurement paralysis. AI can automate data collection for Engagement, Adoption, Retention, and Task Success. |
| **Maturity Level** | Established |
| **Community Adoption** | High |
| **Jerry Sub-Skill Composability** | **Very High** -- 5 dimensions with GSM model per dimension creates a clean, repeatable metrics-setting skill |

**Source:** [HEART Framework](https://www.heartframework.com/); [Google Research Paper](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/); [IxDF HEART](https://www.interaction-design.org/literature/article/google-s-heart-framework-for-measuring-ux)

---

#### 13. UX Honeycomb (Peter Morville)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Peter Morville; created 2004. Morville is the "father of information architecture" |
| **Core Principles** | Seven facets: (1) Useful -- does it serve a purpose?, (2) Usable -- is it easy to use?, (3) Desirable -- is it emotionally engaging?, (4) Findable -- can users find what they need?, (5) Accessible -- can everyone use it?, (6) Credible -- is it trustworthy?, (7) Valuable -- does it deliver value? |
| **Strengths** | Holistic view of UX beyond usability alone; forces teams to consider seven dimensions; highlights often-overlooked facets (Findable, Credible); visual honeycomb format is memorable |
| **Weaknesses** | Descriptive rather than prescriptive -- doesn't specify how to achieve each facet; no built-in measurement; can be used superficially as a checklist; overlap between facets |
| **Tiny Team Applicability** | **High** -- Simple mental model for ensuring coverage. AI can evaluate products against each facet using automated heuristic analysis. |
| **Maturity Level** | Mature |
| **Community Adoption** | High |
| **Jerry Sub-Skill Composability** | **High** -- Seven facets as evaluation dimensions create a natural multi-dimensional assessment skill |

**Source:** [Maze UX Design Frameworks](https://maze.co/collections/ux-ui-design/ux-design-frameworks/); [LogRocket UX Frameworks](https://blog.logrocket.com/ux-design/ux-design-frameworks-types/)

---

#### 14. Five Elements of UX (Jesse James Garrett)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Jesse James Garrett; "The Elements of User Experience" book (2002, 2nd ed. 2010). Garrett also coined "Ajax" for web development |
| **Core Principles** | Five layers from abstract to concrete: (1) Strategy -- user needs + business objectives, (2) Scope -- functional specs + content requirements, (3) Structure -- interaction design + information architecture, (4) Skeleton -- interface design + navigation design + information design, (5) Surface -- visual design |
| **Strengths** | Provides clear mental model for UX complexity; layer separation prevents skipping foundational work; bridges business strategy and visual design; widely taught in UX education |
| **Weaknesses** | Linear/waterfall-ish presentation conflicts with iterative practice; layers are not truly independent; web-centric origins (less adapted to mobile/conversational/AI); static model |
| **Tiny Team Applicability** | **Medium-High** -- The layered model helps tiny teams think systematically about what they might skip. Each layer is a checkpoint. |
| **Maturity Level** | Mature |
| **Community Adoption** | High |
| **Jerry Sub-Skill Composability** | **Medium** -- The five layers are a useful conceptual model but don't provide actionable steps per layer |

**Source:** [ANODA UX Frameworks](https://www.anoda.mobi/ux-blog/top-ux-design-frameworks-for-streamlined-design); [UXPin Design Frameworks](https://www.uxpin.com/studio/blog/design-frameworks/)

---

#### 15. GOMS Model (Card, Moran, Newell)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Stuart Card, Thomas Moran, Allen Newell; 1983 book "The Psychology of Human-Computer Interaction". Variants: KLM (Keystroke-Level Model), NGOMSL, CPM-GOMS |
| **Core Principles** | (1) Goals -- what the user wants to achieve, (2) Operators -- basic actions (keystrokes, clicks, mental operations), (3) Methods -- sequences of operators to achieve goals, (4) Selection Rules -- criteria for choosing among methods |
| **Strengths** | Quantitative predictions of task completion time; formal and scientific; useful for comparing design alternatives objectively; multiple validated variants for different analysis needs |
| **Weaknesses** | Only models skilled, error-free performance; ignores learning, errors, and cognitive load; labor-intensive to construct models; limited to routine tasks; requires expertise to apply |
| **Tiny Team Applicability** | **Low** -- Too specialized and labor-intensive for most tiny team contexts. KLM (simplest variant) could be useful for quick time estimates. AI could potentially automate GOMS analysis. |
| **Maturity Level** | Mature / Legacy |
| **Community Adoption** | Low (academic primarily) |
| **Jerry Sub-Skill Composability** | **Low** -- Highly specialized; KLM could be a micro-tool but the full GOMS suite requires too much expertise |

**Source:** [GOMS Wikipedia](https://en.wikipedia.org/wiki/GOMS); [GOMS Usability BoK](https://www.usabilitybok.org/goms)

---

#### 16. Cognitive Walkthrough

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Cathleen Wharton, John Rieman, Clayton Lewis, Peter Polson; early 1990s at University of Colorado |
| **Core Principles** | (1) Define user goals and tasks, (2) Walk through each step of the interface, (3) At each step ask: Will user know what to do? Will they notice the correct action? Will they understand the feedback?, (4) Focus on learnability for first-time/occasional users |
| **Strengths** | No user recruitment needed; focuses on learnability (often overlooked); identifies issues early in design; low-cost inspection method; complementary to heuristic evaluation |
| **Weaknesses** | Narrow focus on learnability; misses aesthetic, emotional, and performance issues; requires task scenario preparation; evaluator bias possible; tedious for complex interfaces |
| **Tiny Team Applicability** | **High** -- One person can perform a cognitive walkthrough. AI could automate the step-by-step questioning process against a prototype or wireframe. |
| **Maturity Level** | Mature |
| **Community Adoption** | Medium |
| **Jerry Sub-Skill Composability** | **High** -- Clear step-by-step protocol with defined questions at each step maps well to a guided evaluation skill |

**Source:** [NN/g Heuristic Evaluation](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/); [IxDF Heuristic Evaluation](https://www.interaction-design.org/literature/topics/heuristic-evaluation)

---

#### 17. Kano Model

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Professor Noriaki Kano; 1984, Tokyo University of Science |
| **Core Principles** | Classifies features into 5 categories: (1) Basic Needs (must-have), (2) Performance Needs (linear satisfaction), (3) Excitement (delighters), (4) Indifferent (no impact), (5) Reverse (cause dissatisfaction). Uses standardized questionnaire. |
| **Strengths** | Data-driven feature prioritization; reveals non-obvious user preferences; differentiates must-haves from delighters; prevents over-investment in indifferent features; quantitative survey methodology |
| **Weaknesses** | Requires survey design expertise; results change over time (today's delighter becomes tomorrow's basic); questionnaire can confuse participants; sample size requirements; cultural sensitivity |
| **Tiny Team Applicability** | **High** -- Survey-based, scales well. AI can analyze Kano questionnaire responses and auto-classify features. Helps tiny teams focus limited resources on highest-impact features. |
| **Maturity Level** | Mature |
| **Community Adoption** | Medium-High |
| **Jerry Sub-Skill Composability** | **High** -- Standardized questionnaire + classification algorithm = well-defined, repeatable skill |

**Source:** [IxDF Kano Model](https://www.interaction-design.org/literature/article/the-kano-model-a-tool-to-prioritize-the-users-wants-and-desires); [Folding Burritos Kano Guide](https://foldingburritos.com/blog/kano-model/)

---

#### 18. Usability Engineering Lifecycle (Mayhew)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Deborah J. Mayhew; 1999 book "The Usability Engineering Lifecycle" |
| **Core Principles** | Three phases: (1) Requirements Analysis (user profiles, task analysis, usability goals, platform constraints), (2) Design/Testing/Development (three iterative design levels), (3) Installation + feedback collection. Organizational strategies included. |
| **Strengths** | Comprehensive lifecycle coverage; integrates usability into product development; practical engineering focus; includes organizational change strategies; rigorous requirements phase |
| **Weaknesses** | Heavyweight; assumes waterfall-like development; book is dated (pre-Agile, pre-mobile); not widely practiced in modern product teams; high documentation overhead |
| **Tiny Team Applicability** | **Low** -- Full lifecycle is too heavy for tiny teams. Requirements analysis techniques are individually useful. |
| **Maturity Level** | Legacy |
| **Community Adoption** | Low |
| **Jerry Sub-Skill Composability** | **Low** -- Too comprehensive; individual techniques (usability goal setting, task analysis) could be extracted |

**Source:** [Mayhew Usability Engineering Lifecycle](https://www.amazon.com/Usability-Engineering-Lifecycle-Practitioners-Technologies/dp/1558605614)

---

### Category 3: Strategic and Business Frameworks

These frameworks connect UX design to business strategy and value creation.

---

#### 19. Jobs to Be Done (JTBD)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Clayton Christensen (Harvard Business School); Tony Ulwick (Strategyn); evolved from 1990s innovation research. "Milkshake study" is canonical example. Two schools: Christensen's "Switch" school and Ulwick's ODI school |
| **Core Principles** | (1) People "hire" products for specific jobs, (2) Jobs have functional, emotional, and social dimensions, (3) Focus on the job, not the customer demographic, (4) Outcomes are measurable, (5) Competition is anything that gets the same job done |
| **Strengths** | Reframes competition broadly; surfaces unmet needs; transcends demographic segmentation; powerful for innovation; works across B2B and B2C; complementary to personas |
| **Weaknesses** | Abstract -- teams struggle to define "jobs" correctly; two competing schools create confusion; can over-focus on functional jobs; requires skilled facilitation; integration with Agile not straightforward |
| **Tiny Team Applicability** | **High** -- Clarifying the "job" a product serves is essential for small teams who can't afford to build the wrong thing. AI can help map job statements from user interviews. |
| **Maturity Level** | Established |
| **Community Adoption** | High |
| **Jerry Sub-Skill Composability** | **High** -- Job statement template + job map structure = well-defined discovery skill |

**Source:** [User Interviews JTBD Guide](https://www.userinterviews.com/ux-research-field-guide-chapter/jobs-to-be-done-jtbd-framework); [Toptal JTBD Overview](https://www.toptal.com/designers/ux/jobs-to-be-done-framework)

---

#### 20. Outcome-Driven Innovation (ODI)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Anthony (Tony) Ulwick; Strategyn; introduced in Harvard Business Review 2002; expanded in "What Customers Want" (2005) and "Jobs to Be Done" (2016) |
| **Core Principles** | (1) Start with customer-defined outcomes, not ideas, (2) Segment markets by unmet needs, not demographics, (3) Quantify opportunity (importance x satisfaction gap), (4) 1000+ consulting engagements validation, (5) Data-driven front end of innovation |
| **Strengths** | Quantitative approach to innovation; high predictability (claimed 86% success rate); removes guesswork from feature prioritization; reusable customer need inventory; market segmentation by outcome |
| **Weaknesses** | Proprietary methodology (consulting-dependent); expensive to implement fully; requires large-scale surveys; complex analytical framework; can feel overly mechanical |
| **Tiny Team Applicability** | **Medium** -- The outcome-based thinking is valuable; the full quantitative methodology is too heavy. AI could help analyze outcome importance/satisfaction surveys at lower cost. |
| **Maturity Level** | Established |
| **Community Adoption** | Medium |
| **Jerry Sub-Skill Composability** | **Medium** -- Opportunity scoring could be a micro-skill; the full ODI process is consulting-grade heavyweight |

**Source:** [Strategyn ODI](https://strategyn.com/lp/outcome-driven-innovation/); [Ulwick ODI](https://anthonyulwick.com/outcome-driven-innovation/); [ODI Wikipedia](https://en.wikipedia.org/wiki/Outcome-Driven_Innovation)

---

#### 21. UX Strategy (Jaime Levy)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Jaime Levy; book published by O'Reilly (1st ed. 2015, 2nd ed. 2021). Translated into 9 languages |
| **Core Principles** | Four tenets: (1) Business Strategy -- value proposition and growth model, (2) Value Innovation -- new market creation, (3) Validated User Research -- evidence-based decisions, (4) Killer UX Design -- seamless experience. Formula: UX Strategy = Business Strategy + Value Innovation + Validated User Research + Killer UX Design |
| **Strengths** | Bridges UX and business; practical toolkit approach; competitive analysis methodology; validated research emphasis; startup-friendly; updated 2nd edition |
| **Weaknesses** | Startup-biased -- less applicable to enterprise; competitive analysis can be time-consuming; requires strategic thinking beyond typical UX skills; limited community tooling |
| **Tiny Team Applicability** | **Very High** -- Explicitly designed for lean, startup-like contexts. AI can accelerate competitive analysis and market research. |
| **Maturity Level** | Established |
| **Community Adoption** | Medium |
| **Jerry Sub-Skill Composability** | **High** -- Four-tenet framework with competitive analysis toolkit = structured strategy skill |

**Source:** [Jaime Levy UX Strategy](https://jaimelevy.com/ux-strategy-book/); [Netguru UX Strategy Insights](https://www.netguru.com/blog/ux-strategy-insights)

---

#### 22. Experience Design (XD)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Evolved from UX design community, formalized by various practitioners 2015-2020s. APMG International now offers XD Practitioner certification |
| **Core Principles** | (1) Holistic experience across all touchpoints (digital + physical), (2) Journey mapping end-to-end, (3) Emotional design integration, (4) Ecosystem thinking, (5) Cross-channel consistency |
| **Strengths** | Broader than UX -- includes service, brand, and physical experience; journey-centric; growing professional certification; industry recognition; aligns with service design |
| **Weaknesses** | Broad scope can lack focus; overlaps significantly with Service Design and UX; certification relatively new; methodology less codified than Design Thinking; "XD" term overloaded (Adobe XD tool) |
| **Tiny Team Applicability** | **Medium** -- Holistic thinking is valuable but scope may overwhelm tiny teams. Better as a mindset than a methodology for small groups. |
| **Maturity Level** | Emerging |
| **Community Adoption** | Medium |
| **Jerry Sub-Skill Composability** | **Medium** -- Journey mapping and touchpoint audit could be extracted as discrete skills |

**Source:** [NN/g Experience Design](https://www.nngroup.com/articles/experience-design/); [Forrester XD Blog](https://www.forrester.com/blogs/category/experience-design-xd/)

---

### Category 4: Behavioral and Psychological Frameworks

These frameworks model human behavior, motivation, and emotional response.

---

#### 23. Hook Model (Nir Eyal)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Nir Eyal; "Hooked: How to Build Habit-Forming Products" (2014) |
| **Core Principles** | Four-phase cycle: (1) Trigger -- external or internal cue, (2) Action -- simplest behavior in anticipation of reward, (3) Variable Reward -- satisfying craving with unpredictable payoff, (4) Investment -- user puts something in (data, content, reputation) to improve next cycle |
| **Strengths** | Clear model for engagement/retention; explains "sticky" products; practical for product design; well-researched (behavioral psychology + economics); complements Lean/Agile |
| **Weaknesses** | Ethical concerns -- manipulation vs. engagement debate; variable reward can create addiction; primarily suited to consumer products; less relevant for utility/enterprise tools; "dark pattern" risk |
| **Tiny Team Applicability** | **High** -- Simple model, immediately applicable. AI can identify trigger opportunities and test variable reward patterns through A/B testing. |
| **Maturity Level** | Established |
| **Community Adoption** | High |
| **Jerry Sub-Skill Composability** | **High** -- Four-phase model with clear inputs/outputs per phase = natural guided design skill |

**Source:** [Maze UX Frameworks](https://maze.co/collections/ux-ui-design/ux-design-frameworks/); [LogRocket UX Frameworks](https://blog.logrocket.com/ux-design/ux-design-frameworks-types/)

---

#### 24. Fogg Behavior Model (BJ Fogg)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | BJ Fogg, PhD; Stanford Behavior Design Lab; published 2009 at Persuasive Technology conference. Formula: B = MAP (Behavior = Motivation + Ability + Prompt) |
| **Core Principles** | (1) Behavior occurs when M, A, P converge simultaneously, (2) Three Core Motivators (sensation, anticipation, social cohesion), (3) Simplicity factors determine ability, (4) Three prompt types (spark, facilitator, signal), (5) Design for the "prompt" when motivation and ability are sufficient |
| **Strengths** | Scientifically grounded; practical design tool; clear diagnostic framework (if behavior isn't happening, which element is missing?); applicable beyond digital (health, sustainability); influenced Instagram creation |
| **Weaknesses** | Can be used manipulatively; oversimplifies complex behavior; motivation is hard to design for; prompt timing is challenging; doesn't model sustained behavior well |
| **Tiny Team Applicability** | **High** -- Simple diagnostic model. AI can analyze user behavior data to identify which element (M, A, or P) is the bottleneck. |
| **Maturity Level** | Established |
| **Community Adoption** | High |
| **Jerry Sub-Skill Composability** | **High** -- B=MAP formula creates a clear diagnostic/design skill with three evaluation dimensions |

**Source:** [Fogg Behavior Model](https://www.behaviormodel.org/); [Stanford Behavior Design Lab](https://behaviordesign.stanford.edu/resources/fogg-behavior-model)

---

#### 25. Emotional Design (Don Norman)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Don Norman; "Emotional Design: Why We Love (or Hate) Everyday Things" (2004) |
| **Core Principles** | Three processing levels: (1) Visceral -- automatic, appearance-driven ("gut reaction"), (2) Behavioral -- unconscious, usability-driven (function and pleasure of use), (3) Reflective -- conscious, meaning-driven (personal identity, cultural significance, memory) |
| **Strengths** | Bridges aesthetics and usability; explains why attractive things work better; three levels provide actionable design targets; backed by cognitive science; universal applicability |
| **Weaknesses** | Levels overlap in practice; measuring emotional response is hard; cultural variation in visceral reactions; doesn't provide specific design methods; more theoretical than practical |
| **Tiny Team Applicability** | **Medium-High** -- The three-level model is a useful evaluation lens. AI can analyze visual design at the visceral level and user feedback at the reflective level. |
| **Maturity Level** | Mature |
| **Community Adoption** | High |
| **Jerry Sub-Skill Composability** | **Medium** -- Good as an evaluation lens within another methodology; too theoretical for a standalone skill |

**Source:** [IxDF Norman's Three Levels](https://www.interaction-design.org/literature/article/norman-s-three-levels-of-design); [Emotional Design Wikipedia](https://en.wikipedia.org/wiki/Emotional_Design)

---

#### 26. BASIC UX Framework

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | UX practitioners community; focuses on five behavioral dimensions of user experience |
| **Core Principles** | Five evaluation dimensions: (1) Behavioral Impact -- how the product changes user behavior, (2) Affective Impact -- emotional responses, (3) Social Impact -- influence on social interactions, (4) Intellectual Impact -- cognitive engagement, (5) Cognitive Impact -- mental load and comprehension |
| **Strengths** | Multi-dimensional behavioral assessment; considers social and emotional dimensions beyond usability; useful for evaluating products holistically; complements task-focused frameworks |
| **Weaknesses** | Less widely known; limited documentation; overlaps with Emotional Design and UX Honeycomb; measurement methodology not well-defined; academic feel |
| **Tiny Team Applicability** | **Medium** -- Five dimensions provide useful evaluation structure. Less practical guidance on how to measure each dimension. |
| **Maturity Level** | Emerging |
| **Community Adoption** | Low-Medium |
| **Jerry Sub-Skill Composability** | **Medium** -- Five dimensions could be evaluation criteria within a broader assessment skill |

**Source:** [Maze UX Design Frameworks](https://maze.co/collections/ux-ui-design/ux-design-frameworks/); [LogRocket UX Frameworks](https://blog.logrocket.com/ux-design/ux-design-frameworks-types/)

---

#### 27. Octalysis Gamification Framework (Yu-kai Chou)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Yu-kai Chou; developed 2003-2012; published in "Actionable Gamification" (2015). Adopted by Google, LEGO, Tesla, United Nations |
| **Core Principles** | 8 Core Drives: (1) Epic Meaning & Calling, (2) Development & Accomplishment, (3) Empowerment of Creativity, (4) Ownership & Possession, (5) Social Influence & Relatedness, (6) Scarcity & Impatience, (7) Unpredictability & Curiosity, (8) Loss & Avoidance. Left-brain (extrinsic) vs. right-brain (intrinsic) drives; white-hat (positive) vs. black-hat (manipulative) motivation |
| **Strengths** | Comprehensive motivation framework; ethical awareness built in (white-hat vs. black-hat); actionable for game mechanics design; industry adoption; free online tool for scoring |
| **Weaknesses** | Gamification can feel forced if poorly applied; black-hat drives raise ethical concerns; primarily consumer-focused; complex to master all 8 drives; can over-gamify simple products |
| **Tiny Team Applicability** | **High** -- The 8-drive scoring helps tiny teams systematically add engagement mechanics. AI can suggest gamification patterns per drive. |
| **Maturity Level** | Established |
| **Community Adoption** | Medium-High |
| **Jerry Sub-Skill Composability** | **High** -- 8 drives with scoring + white-hat/black-hat evaluation = well-structured engagement design skill |

**Source:** [Octalysis Framework](https://yukaichou.com/gamification-examples/octalysis-gamification-framework/); [IxDF Behavioral Design](https://ixdf.org/literature/topics/behavioral-design)

---

### Category 5: Component and System Architecture Frameworks

These frameworks address how to structure and organize UI components and design systems.

---

#### 28. Atomic Design (Brad Frost)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Brad Frost; methodology published 2013 (blog), book 2016 |
| **Core Principles** | Five levels of UI hierarchy: (1) Atoms -- basic HTML elements (labels, inputs, buttons), (2) Molecules -- simple groups of atoms, (3) Organisms -- complex UI sections, (4) Templates -- page-level layouts, (5) Pages -- specific instances with real content |
| **Strengths** | Creates shared vocabulary for design systems; scalable from small to enterprise; promotes reusability and consistency; clear mental model; widely adopted in design systems |
| **Weaknesses** | Naming metaphor can confuse (chemistry terms feel forced); doesn't address UX process or user research; purely structural -- no methodology for design decisions; can lead to "component-first" thinking |
| **Tiny Team Applicability** | **High** -- Creates systematic design component library that scales. AI can generate and maintain component documentation. Perfect for tiny teams building products that will grow. |
| **Maturity Level** | Established |
| **Community Adoption** | Very High |
| **Jerry Sub-Skill Composability** | **High** -- Five-level component hierarchy with clear creation/audit methodology = natural design system skill |

**Source:** [Atomic Design Book](https://atomicdesign.bradfrost.com/chapter-1/); [Brad Frost Design Systems](https://bradfrost.com/blog/post/a-design-system-governance-process/)

---

#### 29. Gestalt Principles of Perception

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Max Wertheimer, Wolfgang Kohler, Kurt Koffka; Gestalt psychology, early 1900s (Germany). Applied to UX/UI design from 1990s onward |
| **Core Principles** | (1) Proximity -- close objects perceived as grouped, (2) Similarity -- similar elements perceived as related, (3) Closure -- incomplete shapes perceived as complete, (4) Continuity -- elements on a line/curve perceived as related, (5) Figure/Ground -- objects perceived as foreground vs. background, (6) Common Fate -- elements moving together perceived as grouped, (7) Symmetry -- symmetric elements perceived as unified |
| **Strengths** | Scientifically validated perception principles; universal across cultures; directly actionable for layout design; explains why certain designs "feel right"; timeless -- over 100 years of validation |
| **Weaknesses** | Principles can conflict with each other; don't address interaction design (static perception only); require visual design skill to apply; don't cover mobile-specific patterns; more foundational than methodological |
| **Tiny Team Applicability** | **High** -- Fundamental knowledge that improves every design decision. AI can evaluate layouts against Gestalt principles. |
| **Maturity Level** | Mature |
| **Community Adoption** | Very High |
| **Jerry Sub-Skill Composability** | **Medium-High** -- Seven principles as evaluation checklist for visual layout review |

**Source:** [IxDF Gestalt Principles](https://ixdf.org/literature/topics/gestalt-principles); [Figma Gestalt Principles](https://www.figma.com/resource-library/gestalt-principles/)

---

#### 30. Material Design (Google)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Google; launched 2014 at Google I/O; Material Design 3 (Material You) launched 2021 |
| **Core Principles** | (1) Material as metaphor (grounded in physical reality), (2) Bold, graphic, intentional (typography, grids, color, imagery), (3) Motion provides meaning, (4) Adaptive design across platforms, (5) Customizable expression (Material You personalization) |
| **Strengths** | Complete design system with components, guidelines, and code; cross-platform consistency; extensive documentation; open source; active community; Material You adds personalization |
| **Weaknesses** | Google-centric aesthetic; can make all apps look similar; opinionated about visual style; learning curve for full system; may conflict with brand identity goals |
| **Tiny Team Applicability** | **High** -- Provides pre-built components and guidelines, saving design time. AI tools increasingly generate Material-compliant layouts. |
| **Maturity Level** | Established |
| **Community Adoption** | Very High |
| **Jerry Sub-Skill Composability** | **Medium** -- More of a design system to adopt than a methodology to follow; audit/compliance checking is the skill opportunity |

**Source:** [Material Design](https://m3.material.io/); [ANODA UX Frameworks](https://www.anoda.mobi/ux-blog/top-ux-design-frameworks-for-streamlined-design)

---

### Category 6: Accessibility and Ethics Frameworks

These frameworks address inclusive design, accessibility, ethical considerations, and value alignment.

---

#### 31. Microsoft Inclusive Design

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Microsoft Design team; launched 2015; led by Kat Holmes (author of "Mismatch") |
| **Core Principles** | (1) Recognize Exclusion -- identify barriers, (2) Learn from Diversity -- understand unique needs, (3) Solve for One, Extend to Many -- specific solutions with broad benefit. Key insight: design for permanent disabilities creates solutions that benefit everyone (curb cuts, captions, etc.) |
| **Strengths** | Shifts accessibility from compliance to innovation; "permanent, temporary, situational" disability spectrum is powerful; free toolkit; practical guidance; backed by major tech company |
| **Weaknesses** | Microsoft-centric examples; toolkit could be more detailed; measuring inclusive impact is challenging; risk of performative adoption without deep commitment; limited to digital focus |
| **Tiny Team Applicability** | **High** -- The "Solve for One, Extend to Many" principle is efficient. Tiny teams can use the disability spectrum to prioritize accessible features that serve the broadest audience. |
| **Maturity Level** | Established |
| **Community Adoption** | High |
| **Jerry Sub-Skill Composability** | **High** -- Three principles + persona spectrum tool + activity cards = structured inclusive design skill |

**Source:** [Microsoft Inclusive Design](https://inclusive.microsoft.design/); [Microsoft Inclusive Design Toolkit](https://download.microsoft.com/download/b/0/d/b0d4bf87-09ce-4417-8f28-d60703d672ed/inclusive_toolkit_manual_final.pdf)

---

#### 32. Universal Design Principles

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Ronald Mace and team at NC State University; 1997. Originally for architecture and product design, adapted for digital |
| **Core Principles** | Seven principles: (1) Equitable Use, (2) Flexibility in Use, (3) Simple and Intuitive, (4) Perceptible Information, (5) Tolerance for Error, (6) Low Physical Effort, (7) Size and Space for Approach and Use |
| **Strengths** | Foundational accessibility framework; legally referenced (ADA context); applicable beyond digital; promotes "design for all" mindset; well-established in education and policy |
| **Weaknesses** | Originated for physical design (some principles need translation to digital); doesn't provide specific digital guidelines; WCAG more actionable for web/app; can be abstract |
| **Tiny Team Applicability** | **Medium** -- The seven principles are a useful evaluation checklist. For digital products, WCAG provides more actionable guidance. |
| **Maturity Level** | Mature |
| **Community Adoption** | High |
| **Jerry Sub-Skill Composability** | **Medium** -- Seven principles as evaluation criteria; WCAG integration needed for digital specifics |

**Source:** [Section508 Universal Design](https://www.section508.gov/blog/Universal-Design-What-is-it/); [BrowserStack Universal Design](https://www.browserstack.com/guide/universal-design-accessibility)

---

#### 33. Value Sensitive Design (Batya Friedman)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Batya Friedman; University of Washington; developed from 1996; book published by MIT Press (2019) with David Hendry |
| **Core Principles** | Tripartite methodology: (1) Conceptual investigations -- identify stakeholders and values, (2) Empirical investigations -- study user values through research, (3) Technical investigations -- analyze technology implications for values. Includes 17 methods: stakeholder analysis, value scenarios, multilifespan timelines, etc. |
| **Strengths** | Systematic approach to ethics in technology; considers indirect stakeholders; long-term thinking (multilifespan); applicable to AI, robotics, drones, medical devices; academic rigor |
| **Weaknesses** | Academic -- can be slow and expensive; "values" are contested and culturally variable; limited practitioner tooling; integration with Agile is challenging; requires philosophical training |
| **Tiny Team Applicability** | **Low-Medium** -- Full methodology is too heavy. The stakeholder analysis and value scenarios are individually useful and can be done quickly. AI could help map stakeholder values from existing data. |
| **Maturity Level** | Established |
| **Community Adoption** | Low-Medium (primarily academic, growing in AI ethics) |
| **Jerry Sub-Skill Composability** | **Medium** -- Stakeholder value mapping and value scenario methods could be extracted as lightweight skills |

**Source:** [Value Sensitive Design UW](https://ischool.uw.edu/research/impact-stories/value-sensitive-design); [VSD Wikipedia](https://en.wikipedia.org/wiki/Value_sensitive_design)

---

#### 34. REFLECT Framework (Ethical UX)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Master of Design thesis, NIFT Mumbai, 2023-2025. Emerging framework addressing the gap between ethical design ideals and practical implementation |
| **Core Principles** | Incorporates: (1) Empathy in design decisions, (2) Fairness in algorithms and interfaces, (3) Literacy -- user understanding of how products work, (4) Environmental awareness -- digital sustainability, (5) Consent -- transparent data practices. Aims to shift UX "from persuasion to empowerment" |
| **Strengths** | Addresses modern ethical concerns (AI bias, dark patterns, digital sustainability); practical implementation focus; bridges theory and practice; includes consent and environmental dimensions |
| **Weaknesses** | Very new and unproven at scale; limited adoption; academic origin may limit practitioner uptake; overlaps with existing ethical frameworks; not yet widely validated |
| **Tiny Team Applicability** | **High** -- Lightweight ethical checklist. AI can help assess products against REFLECT criteria. Particularly relevant for AI-augmented products. |
| **Maturity Level** | Emerging |
| **Community Adoption** | Low |
| **Jerry Sub-Skill Composability** | **High** -- Five ethical dimensions create a clear evaluation skill for ethical UX review |

**Source:** [ResearchGate REFLECT Framework](https://www.researchgate.net/publication/392579872_ETHICAL_UX_The_REFLECT_Framework_for_Designing_Transparent_Responsible_Sustainable_Digital_Experiences)

---

### Category 7: Operational Frameworks

These frameworks address how design teams operate, scale, and manage their practice.

---

#### 35. DesignOps

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Community-evolved practice, ~2016-2019. Dave Malouf, NN/g, and InVision were early advocates. DesignOps Summit (Rosenfeld Media) has run annually. Term gained traction following DevOps success |
| **Core Principles** | Three pillars: (1) Talent -- hiring, growth, culture, (2) Processes -- rituals, workflows, decision frameworks, (3) Enablers -- tools, assets, design systems. Orchestrates people, processes, and craft to amplify design impact at scale |
| **Strengths** | Addresses operational scaling challenges; 2024 survey shows 87% higher stakeholder satisfaction with established DesignOps; systematizes design team practices; integrates with DevOps/ProductOps |
| **Weaknesses** | Primarily for organizations with 5+ designers; overhead for tiny teams; still evolving as a discipline; varies widely in implementation; requires organizational buy-in |
| **Tiny Team Applicability** | **Low** -- Designed for scaling design teams. Individual principles (standardized tools, reusable assets) are useful but the framework targets larger organizations. |
| **Maturity Level** | Emerging-Established |
| **Community Adoption** | Medium-High |
| **Jerry Sub-Skill Composability** | **Low** -- Organizational framework, not a design methodology; individual practices could inform team setup guidance |

**Source:** [Superside DesignOps Guide](https://www.superside.com/blog/designops-guide); [DesignOps Summit](https://rosenfeldmedia.com/designops-summit/); [Frog DesignOps 101](https://www.frog.co/designmind/designops101)

---

#### 36. ResearchOps

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Kate Towsey coined term in 2018; ResearchOps Community on Slack grew to 16,000+ members in 100+ countries. Community-defined 8 pillars framework |
| **Core Principles** | "People, mechanisms, and strategies that set user research in motion." Eight pillars: (1) Participant Management, (2) Research Scope, (3) Environment, (4) Organizational Context, (5) Data & Knowledge Management, (6) Governance, (7) People (skills & roles), (8) Tools & Infrastructure |
| **Strengths** | Systematizes research logistics; frees researchers for actual research; community-driven standards; 8-pillar checklist identifies bottlenecks; growing adoption |
| **Weaknesses** | Organizational focus (less relevant for tiny teams); still codifying best practices; heavy on logistics, light on methodology; requires dedicated operational role at scale |
| **Tiny Team Applicability** | **Low-Medium** -- The 8 pillars are useful for auditing research practices, but the operational overhead targets larger teams. AI could automate many ResearchOps tasks (participant recruitment, data management). |
| **Maturity Level** | Emerging |
| **Community Adoption** | Medium |
| **Jerry Sub-Skill Composability** | **Low** -- Operational framework; individual pillars (participant management, data management) could inform research skill setup |

**Source:** [Ethn.io ResearchOps Guide](https://ethn.io/blog/research-ops-101); [Maze ResearchOps](https://maze.co/blog/research-ops/); [Great Question ResearchOps 2025](https://greatquestion.co/blog/ux-research-operations-101)

---

### Category 8: Emerging and AI-Native Frameworks

These frameworks address newer design challenges including complex systems, AI integration, and cross-domain experiences.

---

#### 37. Systemic Design

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Interdisciplinary emergence, 2010s. UK Design Council incorporated into revised Double Diamond (2021). Peter Jones and Kristel Van Ael published foundational texts. Systemic Design Toolkit by Namahn/Shift Design |
| **Core Principles** | (1) Acknowledge complexity and interconnectedness, (2) Six activities: framing, formulating, generating, reflecting, inquiring, facilitating, (3) Integrate systems thinking with design thinking, (4) Consider ecological, social, technical, and economic levels, (5) Mindset: inquiring, open, integrative, collaborative, centered |
| **Strengths** | Addresses wicked problems that simpler frameworks cannot; draws from soft systems methodology, critical systems thinking, and cybernetics; institutional recognition (Design Council); applied in healthcare, urban planning, sustainability |
| **Weaknesses** | Steep learning curve; requires systems thinking literacy; can feel abstract and overwhelming; limited practitioner tooling compared to Design Thinking; risk of analysis paralysis |
| **Tiny Team Applicability** | **Low-Medium** -- Systemic thinking is valuable but the methodology targets complex multi-stakeholder initiatives. The mindset principles are universally useful. |
| **Maturity Level** | Emerging |
| **Community Adoption** | Low-Medium |
| **Jerry Sub-Skill Composability** | **Low** -- Too conceptual for a standalone skill; systems mapping exercise could be extracted |

**Source:** [Design Council Systemic Design](https://www.designcouncil.org.uk/our-resources/systemic-design-framework/); [Systemic Design Toolkit](https://www.systemicdesigntoolkit.org/); [Systemic Design Wikipedia](https://en.wikipedia.org/wiki/Systemic_design)

---

#### 38. Activity-Centered Design (Don Norman)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Don Norman; articulated in "Human-centered design considered harmful" (ACM Interactions, 2005). Theoretical roots in Activity Theory (Leontiev, Vygotsky) |
| **Core Principles** | (1) Focus on the activity, not the individual user, (2) Activities are stable; users are many and various, (3) Organize by usage patterns, not logical categories, (4) Design for the job, not the person, (5) Observation and ethnographic methods to understand activities |
| **Strengths** | Addresses limitations of UCD (designing for "average" user); activities are more stable design targets than user preferences; connects well with JTBD; practical examples (blacksmith tool organization) |
| **Weaknesses** | Less well-known than UCD; can neglect individual accessibility needs; tension with personalization trends; limited methodology documentation; Norman himself has nuanced it as complementary to HCD rather than replacement |
| **Tiny Team Applicability** | **Medium** -- Activity mapping is useful for tiny teams. The philosophical distinction from UCD may be less important than practical application. AI can help identify and model user activities from behavioral data. |
| **Maturity Level** | Established |
| **Community Adoption** | Low-Medium |
| **Jerry Sub-Skill Composability** | **Medium** -- Activity mapping methodology could be a standalone research method |

**Source:** [Activity-Centered Design Wikipedia](https://en.wikipedia.org/wiki/Activity-centered_design); [Norman's JND.org](https://jnd.org/logic-versus-usage-the-case-for-activity-centered-design/)

---

#### 39. Service Blueprinting

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | G. Lynn Shostack; Harvard Business Review, 1984. Adapted for modern service design by NN/g and service design community |
| **Core Principles** | (1) Map entire service process (frontstage + backstage), (2) Line of visibility separates customer-visible from internal, (3) Five swim lanes: physical evidence, customer actions, frontstage, backstage, support processes, (4) Identify failure points and wait points, (5) Cross-functional coordination tool |
| **Strengths** | Reveals hidden operational complexity; identifies failure points before they occur; aligns front-end and back-end teams; 40+ years of use; applicable to any service (digital, physical, hybrid) |
| **Weaknesses** | Can become very complex for large services; maintenance challenge as services evolve; requires cross-team participation to build; static representation of dynamic systems; doesn't capture emotional journey |
| **Tiny Team Applicability** | **Medium-High** -- Even tiny teams operate as services. Simplified blueprints help identify operational gaps. AI can help generate initial blueprints from process descriptions. |
| **Maturity Level** | Mature |
| **Community Adoption** | High |
| **Jerry Sub-Skill Composability** | **High** -- Clear template structure with defined swim lanes and notation = well-structured mapping skill |

**Source:** [NN/g Service Blueprints](https://www.nngroup.com/articles/service-blueprints-definition/); [IxDF Service Blueprint](https://ixdf.org/literature/topics/service-blueprint)

---

#### 40. AI-First Design (Emerging)

| Dimension | Details |
|-----------|---------|
| **Origin/Author** | Multiple contributors, 2023-2026. Greg Nudelman ("UX for AI" book, 2025), Adam Fard (AI UX frameworks), industry practitioners. Not yet codified as a single framework |
| **Core Principles** | Emerging principles: (1) Design for AI capabilities and limitations, (2) Multimodal interaction (voice, touch, gesture, visual), (3) Adaptive/personalized experiences, (4) Confidence indicators and uncertainty communication, (5) Human-AI collaboration patterns, (6) Ethical AI guardrails in UX |
| **Strengths** | Addresses the most pressing design challenge of 2025-2026; builds on existing Atomic Design for component extensibility; multimodal thinking; aligns with Gartner AI-native platform trend |
| **Weaknesses** | Not yet codified -- no single authoritative framework; rapidly evolving; limited empirical validation; practitioners learning by doing; tooling still developing |
| **Tiny Team Applicability** | **Very High** -- AI-augmented tiny teams are the target audience. This is the framework that doesn't fully exist yet but is most needed. |
| **Maturity Level** | Emerging |
| **Community Adoption** | Low-Medium (rapidly growing) |
| **Jerry Sub-Skill Composability** | **Very High** -- Emerging but high need. Component patterns (confidence indicators, streaming containers, human-in-the-loop checkpoints) are discrete, teachable elements |

**Source:** [UX for AI Book](https://www.uxforai.com/c/ux-for-ai-book); [Adam Fard AI UX Frameworks](https://adamfard.com/blog/ai-ux-design-framework); [Groovy Web AI UX Trends 2026](https://www.groovyweb.co/blog/ui-ux-design-trends-ai-apps-2026)

---

## L2 -- Deep Analysis

### Overlap and Complementarity Mapping

The 40 frameworks can be organized into three macro-functions that any design effort requires. Effective practice combines one framework from each:

| Macro-Function | What It Answers | Frameworks That Serve It |
|----------------|----------------|--------------------------|
| **Process** (how to work) | What steps to follow, in what order | Design Thinking, Double Diamond, Design Sprint, Lean UX, Agile UX, Contextual Design, IBM EDT, Goal-Directed Design, Participatory Design, UCD |
| **Evaluation** (how to measure) | Is the design good? How to improve? | Nielsen's Heuristics, HEART, UX Honeycomb, Five Elements, GOMS, Cognitive Walkthrough, Kano Model, Usability Engineering Lifecycle |
| **Structure** (how to organize) | What goes where? How do components relate? | Atomic Design, Gestalt Principles, Material Design, Service Blueprinting |

Cross-cutting frameworks (applicable to all three):
- **Strategy:** JTBD, ODI, UX Strategy, Experience Design
- **Behavioral:** Hook Model, Fogg Behavior Model, Emotional Design, BASIC, Octalysis
- **Values:** Microsoft Inclusive Design, Universal Design, Value Sensitive Design, REFLECT
- **Operations:** DesignOps, ResearchOps
- **Emerging:** Systemic Design, AI-First Design, Activity-Centered Design

**Key complementarity pairs:**
- Design Sprint + HEART = rapid design with clear metrics
- Lean UX + JTBD = hypothesis-driven design grounded in real user jobs
- Double Diamond + Nielsen's Heuristics = structured process with built-in quality gates
- Atomic Design + Material Design = component methodology with implementation system
- Fogg Behavior Model + Hook Model = behavior understanding with engagement design
- Microsoft Inclusive Design + REFLECT = accessibility with ethics

**Key competition/overlap:**
- UCD vs. Activity-Centered Design (user focus vs. activity focus -- Norman argues for synthesis)
- JTBD vs. ODI (same theory, different methodologies -- ODI is quantitative, JTBD is qualitative)
- Design Thinking vs. Double Diamond (similar diverge/converge logic, different structure)
- DesignOps vs. ResearchOps (operational scaling, different scope)
- UX Honeycomb vs. BASIC (multi-dimensional evaluation, different dimensions)

### Evolution Timeline

| Era | Frameworks Born | Key Shift |
|-----|-----------------|-----------|
| **Pre-1990: Foundations** | Universal Design (1997 codified), GOMS (1983), Service Blueprinting (1984), Kano (1984) | Engineering/scientific approach to usability |
| **1990s: Usability** | Nielsen's Heuristics (1994), Goal-Directed Design (1995), Contextual Design (1988/1997), UCD (ISO), Value Sensitive Design (1996), Usability Engineering Lifecycle (1999) | Usability as a discipline; engineering rigor |
| **2000s: Experience** | Design Thinking (popularized), Double Diamond (2004), UX Honeycomb (2004), Five Elements (2002), Emotional Design (2004), Activity-Centered Design (2005) | Shift from "usability" to "experience"; emotion matters |
| **2010s: Lean/Agile** | Lean UX (2013), Agile UX (~2010), Design Sprint (2012/2016), Hook Model (2014), Atomic Design (2013), IBM EDT (~2015), Microsoft Inclusive Design (2015), JTBD/ODI (matured), Fogg Behavior Model (2009), Octalysis (2012) | Speed, iteration, behavior, systems |
| **2020s: Systems + AI** | Systemic Design (matured), REFLECT (2023-25), AI-First Design (emerging), DesignOps (matured), ResearchOps (matured), UX Strategy (matured), Experience Design (matured) | Complexity, ethics, AI integration, operations |

**The trajectory is clear:** From engineering-level usability (1980s-90s) to holistic experience (2000s) to lean/agile speed (2010s) to systemic/ethical/AI-aware design (2020s). Each era builds on rather than replaces the previous one.

### AI-Augmentation Readiness Assessment

| Readiness Level | Frameworks | Why |
|----------------|------------|-----|
| **High** (AI can directly accelerate 50%+ of activities) | Nielsen's Heuristics, HEART, Kano Model, Lean UX, Design Sprint, Fogg Behavior Model, Hook Model, Atomic Design, Cognitive Walkthrough, REFLECT | Structured, rule-based, or data-driven. AI can evaluate, generate, and analyze. |
| **Medium** (AI assists 25-50% of activities) | Design Thinking, Double Diamond, JTBD, UX Strategy, Gestalt Principles, Service Blueprinting, Material Design, Octalysis, UX Honeycomb, Five Elements, ODI, IBM EDT, Microsoft Inclusive Design, Experience Design, BASIC, Emotional Design | Mix of creative/empathetic work (hard for AI) and analytical work (natural for AI). |
| **Low** (AI assists <25% of activities) | Contextual Design, Participatory Design, Goal-Directed Design, Value Sensitive Design, Systemic Design, Activity-Centered Design, Agile UX, Usability Engineering Lifecycle, GOMS, Universal Design, DesignOps, ResearchOps | Heavily ethnographic, workshop-dependent, organizational, or requiring deep human judgment. |

### Gap Analysis: What Is NOT Well-Served

| Gap Domain | Description | Impact on Tiny Teams |
|------------|-------------|---------------------|
| **AI-Human Collaboration UX** | No mature framework for designing AI agent interactions, conversational UX with LLMs, or human-in-the-loop workflows | **Critical** -- Tiny teams building with AI need this most |
| **Multimodal Design** | Existing frameworks assume screen-based interaction. Voice, gesture, spatial, and ambient computing lack unified frameworks | **High** -- As AI enables multimodal, teams need design guidance |
| **Micro-Team Design Operations** | DesignOps and ResearchOps target 5+ person teams. No framework optimizes 1-3 person AI-augmented design workflows | **Critical** -- Gartner's "Tiny Teams" trend creates demand |
| **Continuous Design** | Frameworks assume discrete projects. No mature framework for continuous, always-evolving products with AI-driven personalization | **High** -- Modern products never "ship" and stop |
| **Design for Trust** | Existing ethics frameworks address harm prevention but not trust-building in AI-mediated experiences | **Medium** -- Trust is the key differentiator for AI products |
| **Cross-Cultural AI Design** | No framework addresses cultural variation in AI interaction expectations | **Medium** -- Global products need cultural adaptation |

### Recommended Combinations for AI-Augmented Tiny Teams

Based on this survey, the optimal framework stack for a 2-3 person team augmented by AI:

| Layer | Recommended Framework | Rationale |
|-------|----------------------|-----------|
| **Process** | Design Sprint (for new features) + Lean UX (for iteration) | Time-boxed, small-team native, hypothesis-driven |
| **Evaluation** | Nielsen's Heuristics + HEART | Expert evaluation + quantitative metrics; both AI-automatable |
| **Structure** | Atomic Design | Component-based, scalable, AI-maintainable |
| **Strategy** | JTBD | Focuses limited resources on real user needs |
| **Behavior** | Fogg Behavior Model + Hook Model | Clear diagnostic + engagement design |
| **Ethics** | Microsoft Inclusive Design + REFLECT | Accessibility + AI ethics in one practice |
| **Measurement** | Kano Model | Prioritize features with limited resources |

---

## Methodology

### Research Approach
- **Primary method:** Web search across 20+ queries covering different framework categories, time periods, and terminology
- **Source types consulted:** Industry publications (NN/g, IxDF, Maze), academic references (ACM, ResearchGate), practitioner blogs, books, and official framework sites
- **Framework:** 5W1H analysis per framework (Who, What, Where, When, Why, How)

### Source Credibility Assessment
- **HIGH confidence sources:** Nielsen Norman Group, IxDF, official framework websites, peer-reviewed publications, books by framework authors
- **MEDIUM confidence sources:** Practitioner blog posts from established agencies, industry surveys (Gartner)
- **LOW confidence sources:** Individual Medium posts (verified against primary sources where possible)

### Limitations
1. Emerging frameworks (AI-First Design, REFLECT) have limited empirical validation
2. "Community Adoption" assessments are qualitative estimates, not measured metrics
3. "Tiny Team Applicability" ratings are the researcher's synthesis, not empirically validated
4. Some frameworks (GOMS, Usability Engineering Lifecycle) may have niche active communities not captured in general web searches
5. Commercial/proprietary frameworks (Figma's design process, Salesforce Lightning Design System) were excluded as they are design systems rather than methodologies

---

## References

1. [NN/g 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) - Key insight: 30+ years of validated usability principles
2. [Maze UX Design Frameworks](https://maze.co/collections/ux-ui-design/ux-design-frameworks/) - Key insight: Framework categorization and comparison
3. [LogRocket UX Frameworks](https://blog.logrocket.com/ux-design/ux-design-frameworks-types/) - Key insight: 15 framework overview with type classification
4. [HEART Framework](https://www.heartframework.com/) - Key insight: Goals-Signals-Metrics model for UX measurement
5. [GV Design Sprint](https://www.gv.com/sprint/) - Key insight: 5-day time-boxed process proven at scale
6. [IDEO Design Kit](https://www.ideo.com/journal/design-kit-the-human-centered-design-toolkit) - Key insight: 57 HCD methods with Field Guide
7. [IxDF Design Thinking Overview](https://ixdf.org/literature/article/design-thinking-a-quick-overview) - Key insight: Multiple Design Thinking variants cataloged
8. [Design Council Framework for Innovation](https://www.designcouncil.org.uk/our-resources/framework-for-innovation/) - Key insight: Double Diamond with 2019 systemic design update
9. [IBM Enterprise Design Thinking](https://www.ibm.com/design/thinking/page/framework) - Key insight: Hills/Playbacks/Sponsor Users triad for enterprise scale
10. [Microsoft Inclusive Design](https://inclusive.microsoft.design/) - Key insight: "Solve for One, Extend to Many" + disability spectrum
11. [Atomic Design Book](https://atomicdesign.bradfrost.com/chapter-1/) - Key insight: Five-level component hierarchy
12. [Fogg Behavior Model](https://www.behaviormodel.org/) - Key insight: B=MAP formula for behavior design
13. [User Interviews JTBD Guide](https://www.userinterviews.com/ux-research-field-guide-chapter/jobs-to-be-done-jtbd-framework) - Key insight: Functional, emotional, social job dimensions
14. [Strategyn ODI](https://strategyn.com/lp/outcome-driven-innovation/) - Key insight: Quantitative opportunity scoring methodology
15. [Jaime Levy UX Strategy](https://jaimelevy.com/ux-strategy-book/) - Key insight: Four tenets bridging UX and business strategy
16. [Value Sensitive Design UW](https://ischool.uw.edu/research/impact-stories/value-sensitive-design) - Key insight: Tripartite methodology (conceptual, empirical, technical)
17. [Dubberly on Cooper GDD](https://www.dubberly.com/articles/alan-cooper-and-the-goal-directed-design-process.html) - Key insight: Goals vs. tasks distinction; personas as primary tool
18. [Contextual Design Wikipedia](https://en.wikipedia.org/wiki/Contextual_design) - Key insight: Ethnographic field methods since 1988
19. [Participatory Design Wikipedia](https://en.wikipedia.org/wiki/Participatory_design) - Key insight: Scandinavian democratic design tradition
20. [IxDF Gestalt Principles](https://ixdf.org/literature/topics/gestalt-principles) - Key insight: 100+ years of validated perception science
21. [Gartner 2026 Technology Trends](https://www.gartner.com/en/newsroom/press-releases/2025-10-20-gartner-identifies-the-top-strategic-technology-trends-for-2026) - Key insight: AI-native platforms enabling tiny teams
22. [Design Council Systemic Design](https://www.designcouncil.org.uk/our-resources/systemic-design-framework/) - Key insight: Six-activity methodology for complex challenges
23. [Octalysis Framework](https://yukaichou.com/gamification-examples/octalysis-gamification-framework/) - Key insight: 8 core drives with white-hat/black-hat distinction
24. [ResearchGate REFLECT Framework](https://www.researchgate.net/publication/392579872_ETHICAL_UX_The_REFLECT_Framework_for_Designing_Transparent_Responsible_Sustainable_Digital_Experiences) - Key insight: Emerging ethical UX framework bridging ideals and practice
25. [UX for AI Book](https://www.uxforai.com/c/ux-for-ai-book) - Key insight: Emerging AI-specific UX patterns and methodologies
26. [Google Research HEART Paper](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) - Key insight: Large-scale UX measurement at Google
27. [Kano Model IxDF](https://www.interaction-design.org/literature/article/the-kano-model-a-tool-to-prioritize-the-users-wants-and-desires) - Key insight: Feature prioritization by emotional response
28. [NN/g Service Blueprints](https://www.nngroup.com/articles/service-blueprints-definition/) - Key insight: Frontstage/backstage service visualization
29. [Adam Fard AI UX Frameworks](https://adamfard.com/blog/ai-ux-design-framework) - Key insight: Emerging patterns for AI-powered experiences
30. [Superside DesignOps Guide](https://www.superside.com/blog/designops-guide) - Key insight: People/processes/craft orchestration at scale
31. [Maze ResearchOps](https://maze.co/blog/research-ops/) - Key insight: 8 pillars for scaling research operations
32. [NN/g Experience Design](https://www.nngroup.com/articles/experience-design/) - Key insight: XD as evolution beyond UX
33. [IxDF Behavioral Design](https://ixdf.org/literature/topics/behavioral-design) - Key insight: Intersection of psychology and UX
34. [Norman's Three Levels](https://www.interaction-design.org/literature/article/norman-s-three-levels-of-design) - Key insight: Visceral/behavioral/reflective processing
35. [Section508 Universal Design](https://www.section508.gov/blog/Universal-Design-What-is-it/) - Key insight: Seven principles from architecture to digital

---

*Research completed: 2026-03-02 | Agent: ps-researcher | Frameworks cataloged: 40 | Sources cited: 35*
