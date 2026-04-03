# Python Patterns
*Updated: 2026-04-03T15:51:45Z*

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

## Ruff Rules (active)

`pyproject.toml` selects: E, W, F, I, B, C4, UP, S506, TCH, PTH, RUF. Ignores: E501 (line length, handled by formatter), B017 (pytest.raises used intentionally).

- **S506** — ban unsafe YAML APIs (`yaml.load`, `yaml.unsafe_load`)
- **TCH** — typing-only imports must live in `TYPE_CHECKING` blocks to reduce runtime overhead
- **PTH** — use `pathlib.Path` over `os.path`
- **RUF** — ruff-specific: unused `noqa`, unsorted `__all__`, mutable class defaults

## Python Version Support

`pyproject.toml` `requires-python = ">=3.11"`. Classifiers cover 3.11, 3.12, 3.13, 3.14. The active `.venv` uses Python 3.14.

## Related Lode Files

- [testing.md](testing.md) — how patterns are tested
- [../framework/architecture.md](../framework/architecture.md) — layer rules that constrain imports
