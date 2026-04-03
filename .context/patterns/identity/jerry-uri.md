# PAT-ID-003: TomUri Pattern

> **Status**: RECOMMENDED
> **Category**: Identity
> **Also Known As**: Entity URI, Resource Identifier

---

## Intent

Define a standardized URI scheme for cross-system entity references in Tom.

---

## Problem

Without standardized URIs:
- Different systems reference entities differently
- No canonical format exists for external references
- Deep linking into entity hierarchies is inconsistent
- Integration with external tools lacks uniformity

---

## Solution

Define a URI scheme specifically for Tom entities.

### URI Format

```
tom://entity_type/id[/sub_entity/sub_id]

Examples:
tom://task/a1b2c3d4
tom://plan/xyz98765/phase/001
tom://knowledge/pattern/p-001
```

### Implementation

```python
from dataclasses import dataclass
from typing import Optional
import re

@dataclass(frozen=True)
class TomUri:
    """URI-based entity reference for cross-system identification."""
    entity_type: str
    entity_id: str
    sub_entity_type: Optional[str] = None
    sub_entity_id: Optional[str] = None

    def __str__(self) -> str:
        base = f"tom://{self.entity_type}/{self.entity_id}"
        if self.sub_entity_type:
            base += f"/{self.sub_entity_type}/{self.sub_entity_id}"
        return base

    @classmethod
    def parse(cls, uri: str) -> 'TomUri':
        """Parse a tom:// URI string.

        Args:
            uri: URI string in format tom://type/id[/subtype/subid]

        Returns:
            Parsed TomUri instance

        Raises:
            ValueError: If URI format is invalid
        """
        pattern = r'^tom://([^/]+)/([^/]+)(?:/([^/]+)/([^/]+))?$'
        match = re.match(pattern, uri)

        if not match:
            raise ValueError(f"Invalid TomUri format: {uri}")

        return cls(
            entity_type=match.group(1),
            entity_id=match.group(2),
            sub_entity_type=match.group(3),
            sub_entity_id=match.group(4)
        )

    def to_vertex_id(self) -> 'VertexId':
        """Convert to appropriate VertexId subclass."""
        id_mapping = {
            'task': TaskId,
            'phase': PhaseId,
            'plan': PlanId,
            'knowledge': KnowledgeId,
        }
        id_class = id_mapping.get(self.entity_type, VertexId)
        return id_class(self.entity_id)
```

---

## Tom Implementation

### File Location

`src/shared_kernel/identity/tom_uri.py`

### URI Components

| Component | Description | Required |
|-----------|-------------|----------|
| Scheme | Always `tom://` | Yes |
| entity_type | Type of entity (task, plan, phase, knowledge) | Yes |
| entity_id | Primary entity identifier | Yes |
| sub_entity_type | Type of sub-entity | No |
| sub_entity_id | Sub-entity identifier | No |

---

## Use Cases

### 1. Cross-System References

```python
# Reference task in external documentation
uri = TomUri(entity_type="task", entity_id="a1b2c3d4")
# tom://task/a1b2c3d4
```

### 2. Deep Links

```python
# Reference phase within a plan
uri = TomUri(
    entity_type="plan",
    entity_id="xyz98765",
    sub_entity_type="phase",
    sub_entity_id="001"
)
# tom://plan/xyz98765/phase/001
```

### 3. Knowledge References

```python
# Reference a pattern
uri = TomUri(entity_type="knowledge", entity_id="pattern/p-001")
# tom://knowledge/pattern/p-001
```

---

## Consequences

| Type | Consequence |
|------|-------------|
| (+) | Standardized references across systems |
| (+) | Human-readable and self-documenting |
| (+) | Supports hierarchical entity references |
| (+) | Parseable and reconstructible |
| (-) | Additional abstraction layer |

---

## Related Patterns

- [PAT-ID-001: VertexId](./vertex-id.md) - Base identity class
- [PAT-ID-002: Domain-Specific IDs](./domain-specific-ids.md) - Concrete ID types

---

## Design Canon Reference

Lines 170-217 in Tom Design Canon v1.0

---

*Pattern documented by Claude (Opus 4.5) as part of TD-017*
