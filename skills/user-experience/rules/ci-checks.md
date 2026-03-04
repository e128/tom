<!-- VERSION: 1.0.0 | DATE: 2026-03-04 | SOURCE: SKILL.md (skills/user-experience/SKILL.md) Sections "P-003 Compliance", "Wave Transition Quality Gates" | PARENT: /user-experience skill -->

# CI Checks Rules

> CI/CD verification rules for the /user-experience skill. Defines automated checks for P-003 enforcement, schema validation, wave gate compliance, trigger map validation, and output quality verification. See also: `skills/user-experience/rules/wave-progression.md` (wave signoff validation criteria consumed by UX-CI-007/UX-CI-008), `skills/user-experience/rules/synthesis-validation.md` (synthesis confidence gates consumed by UX-CI-011 through UX-CI-013), `skills/user-experience/rules/mcp-coordination.md` (MCP ownership validation consumed by UX-CI-007 kickoff signoff). CI standards: `.context/rules/quality-enforcement.md` [Enforcement Architecture] L5 layer, `.context/rules/agent-development-standards.md` [H-34] (schema validation), [H-35] (constitutional compliance).

## Document Sections

| Section | Purpose |
|---------|---------|
| [P-003 Enforcement](#p-003-enforcement) | No sub-skill agent has Task tool access |
| [Schema Validation](#schema-validation) | Governance YAML validation against JSON Schema |
| [Wave Gate Compliance](#wave-gate-compliance) | Signoff file existence and structure verification |
| [Trigger Map Validation](#trigger-map-validation) | Keyword collision detection for new sub-skills |
| [Output Quality Checks](#output-quality-checks) | Confidence classification and traceability verification |
| [CI Gate Summary](#ci-gate-summary) | All gates with pass/fail criteria |

---

## P-003 Enforcement

<!-- Source: SKILL.md Section "P-003 Compliance" — single-level nesting enforcement. -->
<!-- Source: H-34 (agent definition standards, compound — includes retired H-35 constitutional compliance sub-item b), H-01 (P-003). -->

The `/user-experience` skill enforces strict single-level nesting per H-01/P-003. Only `ux-orchestrator` has Task tool access. All 10 sub-skill agents are workers that MUST NOT include Task in their tool list.

### CI Gate: Task Tool Grep

**Check:** Scan all sub-skill agent `.md` files for Task tool presence in `tools:` frontmatter.

**Scope:** All files matching `skills/ux-*/agents/*.md` (excludes `skills/user-experience/agents/ux-orchestrator.md`).

**Pass criteria:** Zero matches for `Task` in the `tools:` YAML frontmatter field of any sub-skill agent file.

**Implementation pattern:**

```bash
# Extract tools frontmatter from sub-skill agents and check for Task
for agent_file in skills/ux-*/agents/*.md; do
  # Skip the orchestrator (T5, allowed to have Task)
  if [[ "$agent_file" == *"ux-orchestrator"* ]]; then
    continue
  fi
  # Extract YAML frontmatter (content between first two --- delimiters) and check tools field
  tools_line=$(sed -n '2,/^---$/p' "$agent_file" | grep -E '^tools:' | head -1)
  if echo "$tools_line" | grep -q 'Task'; then
    echo "FAIL: $agent_file contains Task in tools frontmatter (P-003 violation)"
    exit 1
  fi
done
echo "PASS: No sub-skill agent has Task tool access"
```

### CI Gate: disallowedTools Declaration

**Check:** All sub-skill agents declare `disallowedTools: [Task]` in their `.md` frontmatter.

**Pass criteria:** Every sub-skill agent `.md` file (matching `skills/ux-*/agents/*.md`, excluding `ux-orchestrator`) contains `disallowedTools` with `Task` listed.

**Implementation pattern:**

```bash
# Verify disallowedTools: [Task] in sub-skill agent frontmatter
for agent_file in skills/ux-*/agents/*.md; do
  if [[ "$agent_file" == *"ux-orchestrator"* ]]; then
    continue
  fi
  # Check for disallowedTools containing Task
  if ! grep -A 5 '^disallowedTools' "$agent_file" | grep -q 'Task'; then
    echo "FAIL: $agent_file missing disallowedTools: [Task] (P-003 enforcement)"
    exit 1
  fi
done
echo "PASS: All sub-skill agents declare disallowedTools: [Task]"
```

### CI Gate: Forbidden Actions Declaration

**Check:** All sub-skill agent `.governance.yaml` files include the constitutional triplet (P-003, P-020, P-022) in `capabilities.forbidden_actions` with minimum 3 entries per H-34(b).

**Pass criteria:** Every `.governance.yaml` file under `skills/ux-*/agents/` contains at least 3 entries in `capabilities.forbidden_actions`, with at least one entry referencing each of P-003, P-020, and P-022.

**Implementation pattern:**

```bash
# Verify constitutional triplet in forbidden_actions
for yaml_file in skills/ux-*/agents/*.governance.yaml; do
  # Count P-0XX references within forbidden_actions section only
  fa_count=$(sed -n '/forbidden_actions:/,/^[a-z]/p' "$yaml_file" | grep -c 'P-0[0-9][0-9]' || true)
  for principle in "P-003" "P-020" "P-022"; do
    if ! grep -q "$principle" "$yaml_file"; then
      echo "FAIL: $yaml_file missing $principle in forbidden_actions"
      exit 1
    fi
  done
  if [ "$fa_count" -lt 3 ]; then
    echo "FAIL: $yaml_file has fewer than 3 forbidden_actions entries"
    exit 1
  fi
done
echo "PASS: All governance files include constitutional triplet in forbidden_actions"
```

---

## Schema Validation

<!-- Source: H-34 (agent definition standards) — dual-file architecture. -->

### CI Gate: Governance YAML Schema

**Check:** All governance YAML files validate against the canonical JSON Schema.

**Scope:** All files matching `skills/ux-*/agents/*.governance.yaml` AND `skills/user-experience/agents/*.governance.yaml`.

**Schema:** `docs/schemas/agent-governance-v1.schema.json`

**Pass criteria:** Zero validation errors across all governance YAML files.

**Implementation pattern:**

```bash
# Validate each governance YAML against JSON Schema
for yaml_file in skills/ux-*/agents/*.governance.yaml skills/user-experience/agents/*.governance.yaml; do
  if ! uv run check-jsonschema --schemafile docs/schemas/agent-governance-v1.schema.json "$yaml_file"; then
    echo "FAIL: $yaml_file fails schema validation"
    exit 1
  fi
done
echo "PASS: All governance YAML files validate"
```

### CI Gate: Required Governance Fields

**Check:** All governance YAML files contain the minimum required fields.

**Required fields:**
- `version` (semantic versioning pattern)
- `tool_tier` (T1-T5 enum)
- `identity.role` (non-empty string)
- `identity.expertise` (array, min 2 entries)
- `identity.cognitive_mode` (enum: divergent, convergent, integrative, systematic, forensic)
- `constitution.principles_applied` (array, min 3 entries, MUST include P-003, P-020, P-022)
- `capabilities.forbidden_actions` (array, min 3 entries)

**Implementation pattern:**

```bash
# Verify required governance fields exist and meet constraints
for yaml_file in skills/ux-*/agents/*.governance.yaml skills/user-experience/agents/*.governance.yaml; do
  # Check version field exists and matches semver pattern
  if ! grep -qE '^version:\s+"?[0-9]+\.[0-9]+\.[0-9]+"?' "$yaml_file"; then
    echo "FAIL: $yaml_file missing or invalid version (must be semver)"
    exit 1
  fi
  # Check tool_tier field exists and is T1-T5
  if ! grep -qE '^tool_tier:\s+"?T[1-5]"?' "$yaml_file"; then
    echo "FAIL: $yaml_file missing or invalid tool_tier (must be T1-T5)"
    exit 1
  fi
  # Check identity.role exists (non-empty string under identity block)
  if ! sed -n '/^identity:/,/^[a-z]/p' "$yaml_file" | grep -qE '^\s+role:\s+".+"'; then
    echo "FAIL: $yaml_file missing identity.role"
    exit 1
  fi
  # Check identity.expertise has at least 2 entries
  expertise_count=$(sed -n '/^\s\+expertise:/,/^\s\+[a-z]/p' "$yaml_file" | grep -c '^\s\+-' || true)
  if [ "$expertise_count" -lt 2 ]; then
    echo "FAIL: $yaml_file has fewer than 2 identity.expertise entries (found $expertise_count)"
    exit 1
  fi
  # Check identity.cognitive_mode is valid enum
  if ! sed -n '/^identity:/,/^[a-z]/p' "$yaml_file" | grep -qE 'cognitive_mode:\s+"?(divergent|convergent|integrative|systematic|forensic)"?'; then
    echo "FAIL: $yaml_file missing or invalid identity.cognitive_mode"
    exit 1
  fi
  # Check constitution.principles_applied has at least 3 entries including P-003, P-020, P-022
  principles_count=$(sed -n '/principles_applied:/,/^[a-z]/p' "$yaml_file" | grep -c '^\s\+-' || true)
  if [ "$principles_count" -lt 3 ]; then
    echo "FAIL: $yaml_file has fewer than 3 constitution.principles_applied entries"
    exit 1
  fi
  for principle in "P-003" "P-020" "P-022"; do
    if ! sed -n '/principles_applied:/,/^[a-z]/p' "$yaml_file" | grep -q "$principle"; then
      echo "FAIL: $yaml_file missing $principle in constitution.principles_applied"
      exit 1
    fi
  done
done
echo "PASS: All governance files contain required fields"
```

### CI Gate: Frontmatter-Governance Consistency

**Check:** The `.md` frontmatter `name` field matches the `.governance.yaml` filename pattern.

**Pass criteria:** For each agent, the `.md` `name` field equals the `.governance.yaml` filename without the `.governance.yaml` extension.

**Implementation pattern:**

```bash
# Verify .md name field matches .governance.yaml filename
for yaml_file in skills/ux-*/agents/*.governance.yaml skills/user-experience/agents/*.governance.yaml; do
  # Derive expected name from governance filename (strip path and .governance.yaml)
  expected_name=$(basename "$yaml_file" .governance.yaml)
  # Find corresponding .md file
  md_file="${yaml_file%.governance.yaml}.md"
  if [ ! -f "$md_file" ]; then
    echo "FAIL: No matching .md file for $yaml_file (expected $md_file)"
    exit 1
  fi
  # Extract name field from .md YAML frontmatter
  actual_name=$(sed -n '2,/^---$/p' "$md_file" | grep -E '^name:\s+' | head -1 | sed 's/^name:\s*//' | tr -d '"' | tr -d "'" | xargs)
  if [ "$actual_name" != "$expected_name" ]; then
    echo "FAIL: $md_file name '$actual_name' does not match governance filename '$expected_name'"
    exit 1
  fi
done
echo "PASS: All agent name fields match governance filenames"
```

---

## Wave Gate Compliance

<!-- Source: skills/user-experience/rules/wave-progression.md [Signoff Requirements] — signoff file validation criteria. See also: skills/user-experience/rules/wave-progression.md [Wave State Tracking] for file-to-state mapping. -->

### CI Gate: Signoff File Structure

**Check:** When a `WAVE-N-SIGNOFF.md` or `KICKOFF-SIGNOFF.md` file exists, it contains all required fields.

**Scope:** Files matching `skills/user-experience/output/*SIGNOFF*.md`.

**Required fields for KICKOFF-SIGNOFF.md:**
- Date (non-empty)
- Signed off by (non-empty)
- Foundation artifacts verified table (all rows present)
- Acceptance criteria checklist (all items checked)
- Authorization field (YES or NO)

**Required fields for WAVE-N-SIGNOFF.md:**
- Date (non-empty)
- Wave number (matches filename)
- Signed off by (non-empty)
- Sub-skills deployed table (all sub-skills for that wave listed)
- Quality gate composite score (>= 0.85)
- Artifacts verified table (all artifacts for that wave listed)
- Acceptance criteria checklist (all items checked)
- Authorization field (YES or NO)

**Implementation pattern:**

```bash
# Validate signoff file structure
signoff_dir="skills/user-experience/output"
for signoff_file in "$signoff_dir"/*SIGNOFF*.md; do
  [ -f "$signoff_file" ] || continue
  filename=$(basename "$signoff_file")

  # Check Date field is non-empty
  if ! grep -qE '^\*\*Date:\*\*\s+\S' "$signoff_file"; then
    echo "FAIL: $signoff_file has empty or missing Date field"
    exit 1
  fi
  # Check Signed off by field is non-empty
  if ! grep -qE '^\*\*Signed off by:\*\*\s+\S' "$signoff_file"; then
    echo "FAIL: $signoff_file has empty or missing Signed off by field"
    exit 1
  fi
  # Check Authorization field contains YES or NO
  if ! grep -qE '(authorized|Authorization).*:\s*(YES|NO)' "$signoff_file"; then
    echo "FAIL: $signoff_file missing Authorization field (must be YES or NO)"
    exit 1
  fi
  # Check all acceptance criteria checkboxes are checked
  unchecked=$(grep -c '\- \[ \]' "$signoff_file" || true)
  if [ "$unchecked" -gt 0 ]; then
    echo "FAIL: $signoff_file has $unchecked unchecked acceptance criteria"
    exit 1
  fi

  # Wave-specific checks
  if [[ "$filename" == WAVE-*-SIGNOFF.md ]]; then
    # Extract wave number from filename
    wave_num=$(echo "$filename" | sed 's/WAVE-\([0-9]\)-SIGNOFF.md/\1/')
    # Verify Wave number field matches filename
    if ! grep -qE '^\*\*Wave:\*\*\s+'"$wave_num" "$signoff_file"; then
      echo "FAIL: $signoff_file Wave number does not match filename (expected $wave_num)"
      exit 1
    fi
    # Verify quality gate composite score exists and is >= 0.85
    score=$(grep -oE 'Composite score:\*\*\s+[0-9]+\.[0-9]+' "$signoff_file" | grep -oE '[0-9]+\.[0-9]+' | head -1)
    if [ -z "$score" ]; then
      echo "FAIL: $signoff_file missing quality gate composite score"
      exit 1
    fi
    # Compare score >= 0.85 using awk (portable decimal comparison)
    if echo "$score" | awk '{exit ($1 >= 0.85) ? 0 : 1}' ; then
      : # score passes
    else
      echo "FAIL: $signoff_file quality gate composite score $score < 0.85"
      exit 1
    fi
    # Verify no FAILED status in sub-skills table
    if grep -qE '\|\s*FAILED\s*\|' "$signoff_file"; then
      echo "FAIL: $signoff_file contains FAILED sub-skill deployment status"
      exit 1
    fi
  fi
done
echo "PASS: All signoff files have valid structure"
```

### CI Gate: Signoff Ordering

**Check:** No WAVE-N-SIGNOFF.md exists without WAVE-(N-1)-SIGNOFF.md existing first.

**Pass criteria:** Signoff files exist in sequential order. WAVE-2-SIGNOFF.md cannot exist without WAVE-1-SIGNOFF.md.

**Exception:** Wave bypass documentation (`wave-bypass-{wave-N}.md`) may exist without the preceding signoff, but carries the bypass warning banner.

**Implementation pattern:**

```bash
# Verify sequential signoff ordering
signoff_dir="skills/user-experience/output"
for wave in 2 3 4 5; do
  prev_wave=$((wave - 1))
  current_file="$signoff_dir/WAVE-${wave}-SIGNOFF.md"
  prev_file="$signoff_dir/WAVE-${prev_wave}-SIGNOFF.md"
  if [ -f "$current_file" ] && [ ! -f "$prev_file" ]; then
    # Check for bypass documentation
    bypass_file="$signoff_dir/wave-bypass-wave-${prev_wave}.md"
    if [ -f "$bypass_file" ]; then
      echo "WARNING: WAVE-${wave}-SIGNOFF.md exists without WAVE-${prev_wave}-SIGNOFF.md (bypass documented)"
    else
      echo "FAIL: WAVE-${wave}-SIGNOFF.md exists without WAVE-${prev_wave}-SIGNOFF.md"
      exit 1
    fi
  fi
done
# Wave 1 requires KICKOFF-SIGNOFF.md
if [ -f "$signoff_dir/WAVE-1-SIGNOFF.md" ] && [ ! -f "$signoff_dir/KICKOFF-SIGNOFF.md" ]; then
  echo "FAIL: WAVE-1-SIGNOFF.md exists without KICKOFF-SIGNOFF.md"
  exit 1
fi
echo "PASS: Signoff files exist in sequential order"
```

---

## Trigger Map Validation

<!-- Source: agent-routing-standards.md RT-M-004 — keyword collision detection. -->

### CI Gate: Keyword Collision Check

**Check:** When a new sub-skill is added (detected by new `skills/ux-*/SKILL.md` file), verify its trigger keywords do not collide with existing skills in `mandatory-skill-usage.md`.

**Implementation:**
1. Extract positive keywords from the new sub-skill's description.
2. Cross-reference against all existing trigger map rows in `mandatory-skill-usage.md`.
3. Flag any keyword that appears in another skill's positive keywords without being in that skill's negative keywords.

**Pass criteria:** Zero unmitigated collisions. Collisions are mitigated by adding the colliding keyword to the appropriate negative keywords list.

**Implementation pattern:**

```bash
# Check for keyword collisions when new sub-skills are added
# This gate runs on PR diff: only when a new skills/ux-*/SKILL.md is added
trigger_map=".context/rules/mandatory-skill-usage.md"
collision_count=0
for skill_file in skills/ux-*/SKILL.md; do
  [ -f "$skill_file" ] || continue
  skill_dir=$(dirname "$skill_file")
  skill_name=$(basename "$skill_dir")
  # Extract description line which contains trigger keywords
  description=$(grep -A 3 'description:' "$skill_file" | head -4)
  # Extract individual words as candidate keywords (lowercase)
  keywords=$(echo "$description" | tr '[:upper:]' '[:lower:]' | tr -cs '[:alpha:]' '\n' | sort -u)
  for keyword in $keywords; do
    # Skip short words (< 4 chars) which are too generic
    [ ${#keyword} -lt 4 ] && continue
    # Check if this keyword appears in another skill's positive keywords row
    # (excluding the /user-experience row itself)
    collision=$(grep -i "$keyword" "$trigger_map" | grep -v '/user-experience' | grep -v '^>' | grep -v '^|--' | head -1 || true)
    if [ -n "$collision" ]; then
      # Check if mitigated by negative keywords
      ux_row=$(grep '/user-experience' "$trigger_map" | head -1)
      neg_keywords=$(echo "$ux_row" | awk -F'|' '{print $3}')
      if ! echo "$neg_keywords" | grep -qi "$keyword"; then
        echo "WARNING: Keyword '$keyword' from $skill_name collides with existing skill"
        collision_count=$((collision_count + 1))
      fi
    fi
  done
done
if [ "$collision_count" -gt 0 ]; then
  echo "WARNING: $collision_count unmitigated keyword collisions detected"
else
  echo "PASS: No keyword collisions detected"
fi
```

### CI Gate: Negative Keyword Coverage

**Check:** The `/user-experience` trigger map row in `mandatory-skill-usage.md` has negative keywords for all skills with > 5 positive keywords (per RT-M-001).

**Pass criteria:** Negative keywords list is non-empty for the `/user-experience` row.

**Implementation pattern:**

```bash
# Verify /user-experience has non-empty negative keywords in trigger map
trigger_map=".context/rules/mandatory-skill-usage.md"
ux_row=$(grep '/user-experience' "$trigger_map" | head -1)
if [ -z "$ux_row" ]; then
  echo "WARNING: /user-experience row not found in trigger map"
  exit 0  # Warning gate, not blocking
fi
# Extract negative keywords column (column 2 in 5-column format)
neg_keywords=$(echo "$ux_row" | awk -F'|' '{print $3}' | xargs)
if [ -z "$neg_keywords" ] || [ "$neg_keywords" = "--" ]; then
  echo "WARNING: /user-experience has empty negative keywords (RT-M-001 violation)"
else
  echo "PASS: /user-experience has non-empty negative keywords"
fi
```

---

## Output Quality Checks

<!-- Source: SKILL.md (skills/user-experience/SKILL.md) Sections "Synthesis Hypothesis Validation", "Cross-Framework Synthesis Protocol" — synthesis output quality enforcement. See also: skills/user-experience/rules/synthesis-validation.md [Synthesis Output Structure] for required sections and format, [Confidence Classification] for gate definitions. Output filename convention: `ux-orchestrator-synthesis.md` for standard synthesis, `ux-orchestrator-crisis.md` for CRISIS mode, per SKILL.md `{topic-slug}` naming convention. -->

### CI Gate: Confidence Classification Presence

**Check:** All synthesis output files contain confidence classifications.

**Scope:** Files matching `skills/user-experience/output/*/ux-orchestrator-synthesis.md` and `skills/user-experience/output/*/ux-orchestrator-crisis.md`.

**Pass criteria:** Every finding in the output includes a confidence classification (HIGH, MEDIUM, or LOW).

**Implementation pattern:**

```bash
# Verify all synthesis findings include confidence classifications
for synthesis_file in skills/user-experience/output/*/ux-orchestrator-synthesis.md \
                      skills/user-experience/output/*/ux-orchestrator-crisis.md; do
  [ -f "$synthesis_file" ] || continue
  # Count findings (lines containing finding IDs like HE-001, BD-002, etc.)
  finding_count=$(grep -cE '^\|.*[A-Z]{2,}-[0-9]{3}' "$synthesis_file" || true)
  if [ "$finding_count" -eq 0 ]; then
    echo "WARNING: $synthesis_file contains no findings to check"
    continue
  fi
  # Count findings that include a confidence classification
  classified_count=$(grep -cE '(HIGH|MEDIUM|LOW)' "$synthesis_file" || true)
  # Each finding row should have a confidence classification
  # Check for finding rows that do NOT have HIGH, MEDIUM, or LOW
  unclassified=$(grep -E '^\|.*[A-Z]{2,}-[0-9]{3}' "$synthesis_file" | grep -vcE '(HIGH|MEDIUM|LOW)' || true)
  if [ "$unclassified" -gt 0 ]; then
    echo "WARNING: $synthesis_file has $unclassified findings without confidence classification"
  fi
done
echo "PASS: Confidence classification check complete"
```

### CI Gate: Traceability

**Check:** All findings in synthesis outputs trace back to a source sub-skill.

**Pass criteria:** Every finding includes a source sub-skill name and source finding ID.

**Implementation pattern:**

```bash
# Verify all synthesis findings include source traceability
for synthesis_file in skills/user-experience/output/*/ux-orchestrator-synthesis.md \
                      skills/user-experience/output/*/ux-orchestrator-crisis.md; do
  [ -f "$synthesis_file" ] || continue
  # Check that findings reference a source sub-skill (e.g., /ux-heuristic-eval)
  finding_lines=$(grep -nE '^\|.*[A-Z]{2,}-[0-9]{3}' "$synthesis_file" || true)
  if [ -z "$finding_lines" ]; then
    continue
  fi
  # Each finding should reference a /ux- sub-skill name
  untraceable=$(echo "$finding_lines" | grep -vcE '/ux-[a-z-]+' || true)
  if [ "$untraceable" -gt 0 ]; then
    echo "WARNING: $synthesis_file has $untraceable findings without source sub-skill traceability"
  fi
  # Each finding should have a source finding ID (e.g., HE-003, BD-001)
  no_source_id=$(echo "$finding_lines" | grep -vcE '[A-Z]{2,}-[0-9]{3}' || true)
  if [ "$no_source_id" -gt 0 ]; then
    echo "WARNING: $synthesis_file has $no_source_id findings without source finding ID"
  fi
done
echo "PASS: Traceability check complete"
```

### CI Gate: LOW Confidence Template Compliance

**Check:** Findings classified as LOW do not contain design recommendations.

**Pass criteria:** Sections tagged `[REFERENCE-ONLY]` do not contain subsections named "Design Recommendations" or "Recommended Actions".

**Implementation pattern:**

```bash
# Verify LOW-confidence sections do not contain design recommendations
for synthesis_file in skills/user-experience/output/*/ux-orchestrator-synthesis.md \
                      skills/user-experience/output/*/ux-orchestrator-crisis.md; do
  [ -f "$synthesis_file" ] || continue
  # Extract sections tagged [REFERENCE-ONLY] and check for forbidden subsections
  # Use awk to capture content between [REFERENCE-ONLY] markers and next ## heading
  ref_only_content=$(awk '/\[REFERENCE-ONLY\]/,/^## /' "$synthesis_file" || true)
  if [ -z "$ref_only_content" ]; then
    continue  # No [REFERENCE-ONLY] sections found
  fi
  # Check for forbidden subsection headings within [REFERENCE-ONLY] content
  if echo "$ref_only_content" | grep -qiE '(Design Recommendations|Recommended Actions)'; then
    echo "WARNING: $synthesis_file contains design recommendations in [REFERENCE-ONLY] section (LOW confidence)"
  fi
done
echo "PASS: LOW confidence template compliance check complete"
```

---

## CI Gate Summary

| Gate ID | Gate Name | Scope | Pass Criteria | Blocking |
|---------|----------|-------|---------------|----------|
| UX-CI-001 | Task Tool Grep | `skills/ux-*/agents/*.md` | Zero Task matches in sub-skill tools | Yes |
| UX-CI-002 | disallowedTools Declaration | `skills/ux-*/agents/*.md` | All sub-skills declare `disallowedTools: [Task]` | Yes |
| UX-CI-003 | Forbidden Actions P-003 | `skills/ux-*/agents/*.governance.yaml` | All governance files reference P-003 | Yes |
| UX-CI-004 | Governance YAML Schema | `skills/ux-*/agents/*.governance.yaml` | Zero schema validation errors | Yes |
| UX-CI-005 | Required Governance Fields | `skills/ux-*/agents/*.governance.yaml` | All required fields present | Yes |
| UX-CI-006 | Frontmatter-Governance Consistency | Agent dual-file pairs | Name field matches filename | Yes |
| UX-CI-007 | Signoff File Structure | `skills/user-experience/output/*SIGNOFF*.md` | All required fields non-empty | Yes |
| UX-CI-008 | Signoff Ordering | `skills/user-experience/output/` | Sequential signoff file existence | Yes |
| UX-CI-009 | Keyword Collision Check | `mandatory-skill-usage.md` | Zero unmitigated collisions | Warning |
| UX-CI-010 | Negative Keyword Coverage | `mandatory-skill-usage.md` | Non-empty negative keywords | Warning |
| UX-CI-011 | Confidence Classification | Synthesis output files | All findings have confidence | Warning |
| UX-CI-012 | Traceability | Synthesis output files | All findings trace to source | Warning |
| UX-CI-013 | LOW Template Compliance | Synthesis output files | No design recs in LOW findings | Warning |

**Blocking:** "Yes" gates fail the CI pipeline. "Warning" gates produce warnings but do not block.

---

*Rule file: ci-checks.md*
*Parent skill: /user-experience*
*Parent SKILL.md: `skills/user-experience/SKILL.md`*
*Sibling rules: `skills/user-experience/rules/ux-routing-rules.md`, `skills/user-experience/rules/synthesis-validation.md`, `skills/user-experience/rules/wave-progression.md`, `skills/user-experience/rules/mcp-coordination.md`*
*Created: 2026-03-03*
*Updated: 2026-03-04*
*Status: COMPLETE*
