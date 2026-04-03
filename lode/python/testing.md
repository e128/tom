# Testing
*Updated: 2026-04-03T00:00:00Z*

BDD test-first development at 90% line coverage (H-20). Tests live in `tests/`.

## Test-First Workflow (H-20)

1. Write a failing test (Red phase) before writing implementation code
2. Write the minimum code to make the test pass (Green phase)
3. Refactor (Refactor phase)

## Running Tests

```bash
uv run pytest tests/                    # all tests
uv run pytest tests/ --cov=src/jerry    # with coverage
uv run pytest tests/ -k "test_session"  # filter by name
```

## Coverage Requirement

90% line coverage is required (H-20). Coverage configuration is in `pyproject.toml`.

## Test Organization

Tests mirror the `src/jerry/` structure:
```
tests/
    domain/
    application/
    infrastructure/
    interface/
    shared_kernel/
```

## Markers

Custom pytest markers are configured in `pyproject.toml`. Use them to tag slow tests, integration tests, etc.

## BDD Style

Tests use descriptive names that describe behavior, not implementation. Use `given/when/then` naming where it improves clarity:

```python
def test_session_start_requires_active_project():
    ...

def test_given_no_project_when_session_start_then_raises_no_active_project_error():
    ...
```

## Related Lode Files

- [patterns.md](patterns.md) — patterns being tested
- [../framework/rules.md](../framework/rules.md) — H-20 coverage requirement
