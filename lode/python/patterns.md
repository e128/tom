# Python Patterns
*Updated: 2026-04-03T14:08:52Z*

Python idioms and patterns used in this codebase.

## Type Hints (H-11)

All public function signatures require type hints. Docstrings are required on public functions. Use `from __future__ import annotations` for forward references.

```python
def create_session(project_id: str, context: SessionContext) -> Session:
    """Create a new work session for the given project.
    
    Args:
        project_id: The PROJ-NNN identifier for the active project.
        context: Session context with user preferences and environment.
    
    Returns:
        A new Session instance in ACTIVE state.
    """
```

## Exception Hierarchy

Domain errors inherit from `DomainError` in `src/shared_kernel/exceptions.py`. Infrastructure errors inherit from their respective base classes. Never catch bare `Exception` — catch specific types.

The full hierarchy (all defined in `src/shared_kernel/exceptions.py`):

| Exception | Signature | Use Case |
|-----------|-----------|----------|
| `DomainError` | `(message)` | Base class |
| `NotFoundError` | `(entity_type, entity_id)` | Entity not found |
| `InvalidStateError` | `(current_state, attempted_action)` | Operation invalid for current state |
| `InvalidStateTransitionError` | `(from_state, to_state)` | State transition not allowed |
| `InvariantViolationError` | `(invariant, details)` | Domain invariant violated |
| `ConcurrencyError` | `(expected_version, actual_version)` | Optimistic concurrency conflict |
| `ValidationError` | `(field, message)` | Input validation failed |

```python
# Correct
except ValidationError as e:
    ...
except NotFoundError as e:
    ...

# Wrong
except Exception:
    ...
```

## Dataclasses

Prefer `@dataclass(frozen=True)` for value objects. Use `@dataclass` for mutable entities. Avoid mutable default arguments.

## Async

Tom uses sync code by default. When async is needed (e.g., external calls), use `asyncio.run()` at the boundary rather than propagating `async` throughout.

## Related Lode Files

- [testing.md](testing.md) — how patterns are tested
- [../framework/architecture.md](../framework/architecture.md) — layer rules that constrain imports
