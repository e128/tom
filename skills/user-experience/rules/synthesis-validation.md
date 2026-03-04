# Synthesis Validation Rules

<!-- STUB: Created during PROJ-022 Foundation phase. Full implementation in EPIC-001. -->

> Validation rules for cross-framework synthesis hypotheses produced by the ux-orchestrator agent. Enforces confidence classification gates (HIGH/MEDIUM/LOW) per P-022.

## Document Sections

| Section | Purpose |
|---------|---------|
| [Confidence Classification](#confidence-classification) | HIGH/MEDIUM/LOW gate definitions |
| [Synthesis Protocol Validation](#synthesis-protocol-validation) | 4-step protocol compliance checks |
| [Convergence Thresholds](#convergence-thresholds) | When findings from multiple frameworks agree |
| [Contradiction Handling](#contradiction-handling) | When frameworks produce conflicting findings |

---

## Confidence Classification

<!-- TODO (EPIC-001): Define confidence gates with thresholds per P-022. -->
<!-- Source: SKILL.md Section "Cross-Framework Synthesis Protocol" defines the 4-step mechanism. -->

Pending implementation. All synthesis hypotheses MUST include confidence classification:
- **HIGH**: 3+ frameworks converge on the same finding
- **MEDIUM**: 2 frameworks converge OR 1 framework with strong evidence
- **LOW**: Single framework finding, weak evidence, or contradiction present

---

## Synthesis Protocol Validation

<!-- TODO (EPIC-001): Define validation checks for each of the 4 synthesis steps. -->

Pending implementation. Validates: Signal Extraction, Convergence Detection, Contradiction Identification, Unified Output.

---

## Convergence Thresholds

<!-- TODO (EPIC-001): Define numeric or categorical thresholds for convergence detection. -->

Pending implementation.

---

## Contradiction Handling

<!-- TODO (EPIC-001): Define how contradictions between frameworks are surfaced to users. -->

Pending implementation. Contradictions MUST be surfaced explicitly per P-022 (no deception).

---

*Rule file: synthesis-validation.md*
*Parent skill: /user-experience*
*Created: 2026-03-03*
*Status: STUB — Full implementation tracked in EPIC-001*
