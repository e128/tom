# Voice Fidelity Score: GitHub Enhancement Issue

## Summary

**Composite Score:** 0.76/1.00 | **Assessment:** Developing
**Strongest Trait:** Technically Precise (0.91) | **Weakest Trait:** Occasionally Absurd (0.52)
**One-line assessment:** The issue preserves technical precision and lands several strong McConkey moments, but deploys skiing metaphors inconsistently -- earned anchors like "the sickest line on the mountain" share space with strained constructions that try too hard, and the warmth dims mid-document to a neutral informational register that loses the collaborator feel.

---

## Scoring Context

- **Text:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
- **Text Type:** documentation (GitHub Enhancement Issue)
- **Audience Context:** documentation
- **Humor Context:** permitted (narrative/vision sections per task brief); no-humor in limitations, tables, and acceptance criteria
- **Calibration Pair:** Pair 5 (Session Start / Presence context) for section tone; Pair 7 (Celebration / Full Energy) for Vision and Research Backing sections
- **Scored:** 2026-03-03T00:00:00Z

---

## Trait Scores

| Trait | Score | Evidence Summary |
|-------|-------|-----------------|
| Direct | 0.78 | Vision section is strong and direct; several mid-document sections develop hedging and corporate transitional structure ("Think of it as...", "Every decision here was a deliberate line choice") |
| Warm | 0.72 | Vision and limitations genuinely treat the reader as a capable peer; long technical description stretches (sub-skill tables, acceptance criteria) go neutral-procedural and lose the collaborator warmth |
| Confident | 0.81 | Confident tone is consistent -- no apology for the scope, limitations section is honest without being defensive; minor softening in "may reflect training data biases" constructions |
| Occasionally Absurd | 0.52 | Several ski metaphors are genuinely earned; others are strained or over-explained; the Vocabulary Reference explicitly flags one pattern found here as a forbidden construction |
| Technically Precise | 0.91 | Every score, agent name, tool tier, wave assignment, cost figure, MCP classification, and acceptance criterion is accurately stated; personality has not displaced any technical content |
| **COMPOSITE** | **0.75** | **(0.78 + 0.72 + 0.81 + 0.52 + 0.91) / 5 = 0.748, rounded to 0.75** |

---

## Detailed Trait Analysis

### Direct (0.78/1.00)

**Evidence:**

Strong moments:
- Vision opener: "Two people. One product. Zero UX specialists." -- no preamble, no hedging, pure McConkey economy
- "Not watered down. Not a chatbot that gives generic advice." -- direct negation that characterizes the thing precisely
- Limitations opener: "We scoped this mountain from every angle. Here is what we found." -- direct, no throat-clearing
- Research Backing opener: "We did not eyeball this line from the lodge. We scoped it from every angle, in every light." -- earned, direct claim

Weaker moments:
- "Every decision here was a deliberate line choice. No shortcuts, no 'we'll figure it out later.'" (Key Design Decisions header) -- the meta-commentary about decision quality is preamble that delays the content
- "Think of it as packing your backcountry kit." (Solution section) -- a softening analogy that delays the direct statement of the architecture
- The Key Design Decisions section uses an introductory framing sentence before each numbered item rather than dropping directly into the substance
- Multiple sections open with question restatements ("What they cannot do:", "Why this matters:") that function as rhetorical preamble before the actual content
- The Vocabulary Reference marks "It's not X. It's Y." as a forbidden construction; several mid-document paragraphs use corrective insertion patterns: "Not watered down. Not a chatbot" is close to this (though it works here); "It does NOT match the throughput" in the honest take is a better example of the pattern appearing where directness would serve better

**Improvement Path:**
Strip the meta-commentary framing sentences that announce what the section is about to say. "Every decision here was a deliberate line choice" is information displacement -- it delays the decisions. Start each numbered design decision directly with the substance. In the Solution section, delete "Think of it as packing your backcountry kit. The orchestrator is the guide who knows the terrain." and let the architecture diagram speak.

---

### Warm (0.72/1.00)

**Evidence:**

Strong moments:
- "This is the UX department a 2-person team never thought they could have." -- genuine identification with the reader's situation
- "McConkey respected the mountain. This is us respecting it. The research gap is real, the architecture accounts for it, and V2 closes it." -- the limitations treatment is warm and honest without being defensive; this reads exactly as a collaborator who takes the problem seriously
- "Two people doing what used to take eight. That is the tiny teams promise." (Capability Map section) -- warm, peer-level framing
- "That is the kind of line scouting that earns the drop-in." (Research Backing close) -- the warmth here is earned by the substance of what preceded it

Where warmth collapses:
- The long sub-skill table sections (10 individual sub-skill descriptions) are technically thorough but read as reference documentation rather than conversation. The "What AI does / What humans do" structure is functional but not warm -- it produces a parallel-structure-formula register (flagged in llm-tell-patterns.md) that feels templated rather than genuine.
- The Acceptance Criteria section drops entirely to checkbox-format with no warmth at all -- which is appropriate for acceptance criteria, but the cold register that precedes it in the V2 Roadmap and Architecture Evolution sections is unnecessary.
- "The missing piece is the **middle layer**" -- this is the vocabulary of a product brief or consultant pitch, not a collaborator

**Improvement Path:**
The warmth is present but front-loaded. The Vision and Limitations sections carry it; the middle sections (sub-skill detail, architecture decisions) go neutral. Two targeted additions would lift this score: (1) a brief collaborator-register sentence opening each Wave group introduction rather than diving directly into tables; (2) vary the "What AI does / What humans do" section openings slightly so they do not read as template-generated parallel structure across all 10 sub-skills.

---

### Confident (0.81/1.00)

**Evidence:**

Strong moments:
- "Built on frameworks that have been battle-tested across thousands of products over the past three decades." -- asserts the quality system without apology
- The limitations section is a confident treatment: it does not apologize for the gaps, it names them honestly and describes the mitigations with specificity. This is exactly the McConkey-respected-danger pattern.
- "The trust argument: not that the analysis is perfect, but that it has been systematically attacked from nine different angles and survived." -- this is strong confident voice; it makes a specific claim about what earned the confidence
- "This portfolio does NOT include a dedicated user research framework." -- no hedging, states the gap flatly
- "AI-generated user insights -- personas, job statements, assumption maps -- are hypotheses, not validated findings." -- direct, no softening

Where confidence weakens slightly:
- "may reflect training data biases" (Synthesis Hypothesis section) -- "may reflect" is hedging. If the concern is real, assert it: "reflect training data biases, not your specific users."
- "potentially to 14-16" (Scope Creep section) -- "potentially" is unnecessary hedging. The architecture analysis either says 14-16 is the projected count or it does not.
- The conditional framing around AI-First Design (CONDITIONAL, projected, Blocking prerequisite) is appropriately specific, not a confidence problem -- the voice handles the conditionality directly.

**Improvement Path:**
The confidence score is already solid. The two specific improvements are: replace "may reflect training data biases" with a direct assertion of the limitation, and remove "potentially" from the scope creep section. Both are single-word edits. The overall confident register is well-maintained throughout.

---

### Occasionally Absurd (0.52/1.00)

**Evidence:**

Earned moments (these work):
- "The sickest line on the mountain is the one nobody thought was skiable. This is that line for tiny teams and UX." (Vision) -- the metaphor is earned, the comparison is precise, it is not explained. Score-worthy.
- "That is the equivalent of standing at the top of a line you scouted from every angle, strapped in with the best gear on the market, and then skiing it with your eyes closed." (Problem section) -- extended metaphor that works because it is specific and the parallel to the problem is exact. Slightly long but earns its length.
- "McConkey respected the mountain. This is us respecting it." (Limitations) -- this is the ideal use of the persona: one sentence, no ski vocabulary explained, the context makes it land. Perfect deployment.
- "That is the kind of line scouting that earns the drop-in." (Research Backing) -- tight, earned, the prior paragraph justifies it.

Strained or over-explained moments (these do not work):
- "Think of it as packing your backcountry kit. The orchestrator is the guide who knows the terrain. The 10 sub-skills are the gear. You do not carry all 10 on every run -- you carry what the mountain demands." (Solution section) -- the metaphor is over-extended and explicitly explained in three sentences. The vocabulary-reference flags explained metaphors as a failure mode. McConkey's line about the backcountry would not require a three-sentence glossary.
- "You do not bring the entire quiver to a powder day. You bring the fat skis. Same principle." (Design Decisions #1) -- two short parallel sentences followed by "Same principle" is the staccato-emphasis-pairs pattern explicitly flagged in vocabulary-reference.md as a forbidden construction. "Every time. Across every model." is the canonical example; "You do not bring the entire quiver to a powder day. You bring the fat skis. Same principle." matches the pattern exactly.
- "Each wave is a progressively steeper run. You earn the next one." (Wave Deployment) -- "You earn the next one" is a staccato emphasis sentence used as rhetorical period. This pattern is in the forbidden constructions list.
- The line "We did not eyeball this line from the lodge. We scoped it from every angle, in every light." (Research Backing header) -- this works better than the others because it is functional (it introduces the research section), but the sentence after it ("We scoped it from every angle, in every light.") repeats the same claim with no added precision, which is redundant.

Pattern analysis: The text deploys skiing vocabulary in approximately 8-10 places. Four of those deployments are earned and tight. Four have the over-extension or staccato-pair pattern that the vocabulary reference explicitly flags as forbidden or weak. This split -- half earned, half strained -- places the score in the 0.50-0.69 range.

**Improvement Path:**
Delete the three-sentence backcountry-kit metaphor explanation in the Solution section and replace with a single image ("Pack what the mountain demands"). Delete "Same principle" from the quiver line -- the analogy works without the explicit label. Delete "You earn the next one" from Wave Deployment -- the table communicates the same thing. Each of these is a deletion, not a rewrite. Four tight ski moments in a 900-line document is enough; the goal is not more skiing vocabulary, it is better-calibrated deployment of what is already there.

---

### Technically Precise (0.91/1.00)

**Evidence:**

This is the strongest trait in the document. Evidence for the high score:

- Every sub-skill score is stated precisely (9.25, 8.05, 8.25, 8.30, 8.55, 8.00, 7.45, 7.50, 8.65, 7.80(P)) with corresponding wave assignments and cognitive mode classifications
- Agent names, tool tiers (T2/T3/T5), and MCP classifications (Official/Bridge/Community) are specific and consistent throughout
- The confidence gate protocol (HIGH/MEDIUM/LOW) specifies exact behaviors: "LOW-confidence outputs structurally omit design recommendation sections" -- not "may omit" or "could omit"
- The limitations section is technically precise: "Figma MCP is required for 4 sub-skills and enhances 2 more (6 of 10 total connections)" -- the count is specific and can be verified against the MCP integration diagram
- Cost figures are specific: "$15/editor/month (Professional)", "$8/member/month (Team plan)", "$99/month (Team plan)"
- The adversarial tournament stats are exact: "Eight iterations. Thirteen revisions."
- The Architecture Evolution Path uses specific thresholds: "at 15+ sub-skills: evaluate Layer 2", "at 20+ sub-skills: evaluate LLM-as-Router" -- consistent with Jerry's scaling roadmap thresholds

Minor precision issues:
- "15-20% of users with disabilities, plus the situational impairments that affect everyone" -- "15-20%" is a well-sourced range but is stated without a citation in the inline text (the research backing section covers sourcing in aggregate but not per-claim)
- The Onboarding warning quoted text ("IMPORTANT: This skill portfolio does NOT include...") is formatted as a blockquote, which slightly ambiguates whether it is descriptive (this is what it says) or prescriptive (this is what it should say). Minor issue.

The voice has not displaced any technical content. Every table, diagram, and acceptance criterion is intact and accurate.

**Improvement Path:**
Technical precision is already at a high level. The only addition that would push this to 0.95+ is inline source citations for the statistical claims in The Problem section (the 15-20% disability stat, the Gartner Tiny Teams trend, the Midjourney/Bolt.new figures). These are currently aggregated in the Research Backing section rather than pointed at their specific claims. Minor refinement, not a significant gap.

---

## Improvement Recommendations (Priority Ordered)

| Priority | Trait | Current | Target | Recommendation |
|----------|-------|---------|--------|----------------|
| 1 | Occasionally Absurd | 0.52 | 0.72 | Delete three forbidden constructions: (a) the three-sentence backcountry-kit metaphor explanation -- cut to one image, (b) "Same principle." after the quiver analogy -- the analogy closes itself, (c) "You earn the next one." in Wave Deployment -- redundant with table content. These are pure deletions. |
| 2 | Warm | 0.72 | 0.82 | Break the 10x parallel "What AI does / What humans do" template pattern. Vary the opening word in at least 4-5 of the sub-skill descriptions. Add one collaborator-register sentence to the Wave 1 and Wave 3 introductions -- these are currently table-first with no warmth before the content. |
| 3 | Direct | 0.78 | 0.84 | Strip meta-commentary framing sentences: delete "Every decision here was a deliberate line choice. No shortcuts, no 'we'll figure it out later.'" and start the design decisions section directly with Decision #1. Similarly, delete "Think of it as packing your backcountry kit." from the Solution section and let the diagram do the work. |
| 4 | Confident | 0.81 | 0.86 | Two single-word edits: replace "may reflect training data biases" with "reflect training data biases" in the Synthesis Hypothesis section; remove "potentially" from the Scope Creep section. Both are hedging words that weaken assertions that deserve confidence. |

---

## Boundary Violation Check

CLEAR. No boundary violations detected.

The limitations section correctly deploys no humor -- "McConkey respected the mountain" is a direct statement of honest assessment, not comedy. The acceptance criteria section is appropriately zero-humor. Tables and technical reference material throughout are appropriately precise with no personality deployed where it would displace information. No cases of bro-culture-adjacent language. No sarcasm directed at the problem or the developer. Boundary conditions are respected.

---

## Leniency Bias Check

- [x] Each trait scored independently
- [x] Evidence documented for each score
- [x] Uncertain scores resolved downward (Occasionally Absurd resolved to 0.52 rather than 0.60 based on four specific prohibited pattern instances; Warm resolved to 0.72 rather than 0.75 based on the 10x parallel structure formula across sub-skill descriptions)
- [x] First-rewrite calibration considered -- this is the initial voice-transformed version; 0.75 is consistent with the expected 0.60-0.75 first-rewrite range (upper end, given the Vision and Limitations sections are well-calibrated)
- [x] No trait scored above 0.95 without exceptional evidence (Technically Precise scored 0.91, which is justified by the comprehensive specific evidence above)

---

## Profile Shape Analysis

This is a **spiked profile** with Technically Precise as the dominant trait and Occasionally Absurd as the suppressed trait.

The pattern is: the rewrite has correctly protected all technical content (the precision is excellent) and has applied McConkey voice mostly to the narrative sections. The suppression issue is not that skiing metaphors are absent -- there are 8-10 of them -- but that approximately half are over-explained or match forbidden construction patterns that exist precisely because they are recognizable LLM-generated voice approximations rather than genuine persona voice.

The document reads like a well-informed attempt at the voice applied to a complex technical document, where the author correctly identified which sections need personality (Vision, Problem, Limitations, Research Backing) but slightly over-indexed on metaphor density in those sections, creating the strained-alongside-earned split that characterizes a 0.52 Occasionally Absurd score.

The strong Technical Precision and Confident scores mean the foundation is sound. The delta between current (0.75) and a strong rewrite (0.85+) is achievable with targeted deletions and minor structural variation -- not a ground-up rewrite.
