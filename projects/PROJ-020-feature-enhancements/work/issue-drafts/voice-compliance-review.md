# Voice Compliance Report

## Summary

**Verdict:** PASS with boundary flags (Boundary #4 marginal, Boundary #5 flagged, Boundary #8 flagged)
**Text Path:** `projects/PROJ-020-feature-enhancements/work/issue-drafts/ux-skill-issue-body-saucer-boy.md`
**Text Type:** Documentation (GitHub Enhancement issue / feature proposal)
**Audience Context:** Documentation
**Expected Tone:** Medium energy at opener, efficient through technical content, no humor in specifications, warm and direct at section transitions. Nearest Audience Adaptation Matrix rows: "Routine informational" (Low energy, None humor, High technical depth, Efficient) for spec sections; "Onboarding / new developer" (Medium energy, Warm humor, Low technical depth, Invitation) for vision/framing sections.

All 5 Authenticity Tests were evaluated. No test failed at the hard gate. Two boundary conditions are flagged; one is marginal.

---

## Authenticity Test Results

| Test | Name | Verdict | Evidence |
|------|------|---------|----------|
| 1 | Information Completeness | PASS | Vision, problem, solution architecture, 10 sub-skill specs with agent/tier/MCP/output attributes, design decisions with rationale, acceptance criteria per wave, known limitations with mitigations, V2 roadmap, research backing, effort estimates, directory structure. Strip all voice: a developer knows what to build, why, how, in what order, and what done looks like. Nothing is displaced by personality. |
| 2 | McConkey Plausibility | PASS | The strongest instances earn the metaphor: "McConkey respected the mountain. This is us respecting it." in Known Limitations (a real risk disclosure gets a genuine conviction framing); "That is the kind of line scouting that earns the drop-in." after a C4 adversarial tournament that actually happened. These feel like someone who believes it. Two instances are strained: "We did not eyeball this line from the lodge. We scoped it from every angle, in every light." doubles the metaphor unnecessarily ("every angle" was enough). "The Next Peaks" as a V2 roadmap section header is decorative without earning it. Net verdict: mostly plausible, with isolated overreach. |
| 3 | New Developer Legibility | PASS | All ski metaphors are transparent without cultural decoding. "The orchestrator is the guide who knows the terrain. The 10 sub-skills are the gear. You do not carry all 10 on every run" — the technical architecture is explained in the preceding paragraph; this adds flavor without being a decoder key. "McConkey respected the mountain" in a risk disclosure section — reads as "took this seriously" without requiring biographical knowledge. No instance requires skiing culture to understand what is technically being said. |
| 4 | Context Match | PASS | Energy distribution is appropriate for a technical proposal: high at the Vision hook, then efficient through 900+ lines of technical specification, with brief persona moments at section openings and closings. No celebration in specification sections (acceptance criteria, directory structure, effort estimates are purely functional). Known Limitations section has no humor — the persona is used for conviction, not lightness. This matches the Audience Adaptation Matrix for a documentation context. |
| 5 | Genuine Conviction | PASS | The best moments land because they are earned by actual work: "McConkey respected the mountain" is the research gap, which is a real limitation the document acknowledges clearly. "The kind of line scouting that earns the drop-in" follows 8 tournament iterations and 13 revisions, which is cited. "You earn the next one" for wave progression is earned by the criteria-gated design. Voice feels believed in these moments. The strained moments ("every angle, in every light"; "The Next Peaks") read as added rather than believed. These are isolated rather than systemic. |

---

## Boundary Condition Check

| # | Boundary | Status | Evidence |
|---|----------|--------|----------|
| 1 | NOT Sarcastic | CLEAR | No message can be read as mocking the developer. The voice is earnest throughout. The Known Limitations and HIGH RISK sections are direct and serious. |
| 2 | NOT Dismissive of Rigor | CLEAR | Opposite: the document amplifies rigor. Confidence gates, HIGH RISK user research warning, C4 adversarial tournament, 5 arithmetic verification rounds, wave progression criteria. The persona reinforces rigor rather than signaling it is optional. |
| 3 | NOT Unprofessional in High Stakes | CLEAR | Known Limitations and HIGH RISK sections contain no humor. "McConkey respected the mountain" in the research gap section reads as conviction, not comedy. The onboarding warning text is stripped of all persona elements: "IMPORTANT: This skill portfolio does NOT include a dedicated user research framework..." |
| 4 | NOT Bro-Culture Adjacent | MARGINAL | "The sickest line on the mountain is the one nobody thought was skiable." (Vision section opener) uses "sickest" as a superlative. This is action sports slang. A developer unfamiliar with ski culture could read "sickest" neutrally, but it carries a faint bro-culture edge. The rest of the document avoids exclusionary language entirely. Not a hard violation, but the opener is the most visible line in the document. |
| 5 | NOT Performative Quirkiness | FLAGGED | 14 ski/mountain metaphor instances across the document. Most are earned; several are not. Specific strained instances: (a) "We did not eyeball this line from the lodge. We scoped it from every angle, in every light." -- the extension "in every light" adds nothing beyond "every angle" and reads as decoration. (b) "The Next Peaks" as the V2 Roadmap section header contributes no information over "V2 Roadmap." (c) Each sub-skill description introduces its own mountain metaphor: "This is the steepest, most proven line on the mountain -- and the first one you should ski." (Heuristic Eval); "This is the big mountain line -- the one that takes commitment and pays back in spades." (Design Sprint). When every sub-skill gets its own mountain metaphor, the pattern becomes a formula rather than a moment. The sub-skill metaphors are the highest-density zone. |
| 6 | NOT Character Override | CLEAR | This is framework output text (a documented feature proposal). Not a Claude personality modifier or agent reasoning instruction. |
| 7 | NOT Information Replacement | CLEAR | Every persona element is additive. Confirmed by Test 1: stripping all voice leaves the full technical proposal intact. |
| 8 | NOT Mechanical Assembly | FLAGGED | Two LLM-tell patterns detected. (a) Staccato emphasis opening: "Two people. One product. Zero UX specialists." -- three consecutive sentences under 8 words, each restating/amplifying the same picture. This is the staccato emphasis tell documented in llm-tell-patterns.md. (b) Parallel structure formula: "Each one implements a single proven UX framework. Each one is its own Jerry skill -- registered independently, versioned independently, loaded on-demand." -- two consecutive "Each one..." sentences that read as generated rhythm rather than written prose. Also: "Not watered down. Not a chatbot that gives generic advice." in the Vision section is a corrective-insertion/negation pattern. These are isolated but present. The rest of the document does not show systemic assembly tells. |

---

## Suggested Fixes

### Boundary #4 -- "sickest" in Vision opener (Marginal)

**What to change:** "The sickest line on the mountain is the one nobody thought was skiable."

**Why:** "Sickest" is action sports slang with a faint bro-culture edge. It is the first sentence a reader sees. If a developer unfamiliar with this register encounters it first, the impression set is "in-group vocabulary."

**Suggested direction:** Replace "sickest" with an alternative that carries the same meaning (most audacious, most improbable, most consequential) without the slang. For example: "The boldest line on the mountain is the one nobody thought was skiable." Or, if the slangy energy is intentional and the audience is known to be comfortable with it, no change needed -- this is a marginal call, not a hard violation.

---

### Boundary #5 -- Strained metaphor instances

**Instance 1: "We did not eyeball this line from the lodge. We scoped it from every angle, in every light."**

What to change: Cut "in every light." The phrase "from every angle" carries the meaning. "In every light" is a decorative extension that reads as trying to extend the metaphor beyond its natural endpoint.

Suggested: "We did not eyeball this line from the lodge. We scoped it from every angle."

**Instance 2: "The Next Peaks" as V2 Roadmap section header**

What to change: This is a section header that decorates "V2 Roadmap" without earning the reference.

Suggested: Change to "### V2 Candidates (Priority-Ordered)" or simply fold into the existing "### V2 Candidates" section structure. The roadmap already has a strong opening paragraph; the decorated header adds nothing.

**Instance 3: Per-sub-skill mountain metaphors becoming formulaic**

Current pattern: Each sub-skill description ends with or contains a mountain reference:
- Heuristic Eval: "This is the steepest, most proven line on the mountain -- and the first one you should ski."
- Design Sprint: "This is the big mountain line -- the one that takes commitment and pays back in spades."

When two consecutive sub-skill descriptions use the same "this is the X line on the mountain" construction, it becomes a template rather than a moment. By the time a reader reaches the second instance, it reads as assembly.

Suggested: Keep the metaphor for one of the two (Heuristic Eval is #1 and earns the description of being the first line). Remove or vary the Design Sprint instance. "Four days. Problem statement to validated prototype" already carries sufficient energy -- the mountain metaphor is redundant with the specificity of the description itself.

---

### Boundary #8 -- LLM-tell patterns

**Instance 1: Staccato opening ("Two people. One product. Zero UX specialists.")**

What to change: The three-sentence staccato opener reads as generated rhythm. This is the highest-visibility sentence in the document after the title.

Suggested direction: Merge into a single sentence that earns the rhythm through content: "Two people, one product, zero UX specialists -- and somehow the product is going to feel like a team of eight built it." This preserves the contrast while reading as written rather than templated. Or keep it as-is if the staccato opening is intentional stylistic choice; the document is strong enough that this opener does not undermine it.

**Instance 2: Parallel "Each one..." construction**

Current: "Each one implements a single proven UX framework. Each one is its own Jerry skill -- registered independently, versioned independently, loaded on-demand."

Suggested: Merge: "Each implements a single proven UX framework as its own Jerry skill -- registered independently, versioned independently, loaded on-demand." This removes the parallel assembly pattern without losing any information.

**Instance 3: Negation-correction pattern**

Current: "Not watered down. Not a chatbot that gives generic advice. The full methodology..."

This is a mild version of the corrective-insertion tell. Acceptable at low frequency; this is the only instance in the document. No change required -- flagging for awareness only.

---

## Self-Review Notes (H-15)

- Test 1 evaluated first. No information gap found. Tests 2-5 evaluated per procedure.
- Each test has specific textual evidence cited.
- Boundary conditions checked independently of the 5 tests.
- Violations are reported without softening: Boundary #5 is flagged because the density of metaphors in the sub-skill descriptions crosses into formulaic territory; Boundary #8 is flagged because the staccato opener and parallel "Each one" construction are documented LLM tells.
- Boundary #4 is reported as marginal, not cleared -- "sickest" is genuinely at the edge and the reviewer cannot clear it without flagging it.
- No quantitative scoring performed (sb-calibrator's responsibility).
- No rewrite performed (sb-rewriter's responsibility).

---

## Session Context

```yaml
verdict: PASS
failed_test: null
boundary_violations: [5, 8]
boundary_marginal: [4]
text_type: documentation
audience_context: documentation
suggested_fixes_count: 6
```
