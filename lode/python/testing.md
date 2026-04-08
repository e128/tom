# Testing
*Updated: 2026-04-07T23:59:58Z*

BDD test-first development. H-20 requires 90% line coverage; CI enforces 80% via `--cov-fail-under=80` (threshold gap tracked separately). Tests live in `tests/`. (`pyproject.toml` `testpaths` also references `scripts/tests/` but that directory does not exist.)

## Test-First Workflow (H-20)

1. Write a failing test (Red phase) before writing implementation code
2. Write the minimum code to make the test pass (Green phase)
3. Refactor (Refactor phase)

## Running Tests

```bash
uv run pytest tests/                    # all tests
uv run pytest --cov=src --cov-report=term-missing  # with coverage
uv run pytest tests/ -k "test_session"  # filter by name
```

## Coverage Requirement

H-20 requires 90% line coverage. CI currently enforces 80% via `--cov-fail-under=80` in `.github/workflows/ci.yml`. Coverage configuration is in `pyproject.toml`.

## Test Organization

```
tests/
    unit/               # fast unit tests by domain
    features/           # Gherkin .feature files (pytest-bdd)
    integration/        # tests with external dependencies
    contract/           # API contract tests
    e2e/                # full end-to-end tests (slow)
    architecture/       # architectural constraint tests
    security/           # security/adversarial scenarios
    regression/         # regression test suites
    bootstrap/          # bootstrap/composition root tests
    fixtures/           # shared test fixtures
    hooks/              # hook tests
    infrastructure/     # infrastructure layer tests
    interface/          # CLI/interface layer tests
    llm/                # LLM integration tests
    project_validation/ # project validation tests
    schemas/            # schema validation tests
    system/             # system-level tests
    session_management/
    work_tracking/
    shared_kernel/
```

## Markers

Markers are configured in `pyproject.toml`:

| Marker | Purpose |
|--------|---------|
| `happy-path` | Happy path scenarios |
| `negative` | Negative/error scenarios |
| `edge-case` | Edge case scenarios |
| `boundary` | Boundary value scenarios |
| `e2e` | End-to-end tests (slow, full stack) |
| `integration` | Integration tests (external dependencies) |
| `subprocess` | Tests that invoke external processes |
| `security` | Security/adversarial scenarios |
| `regression` | Regression scenarios |

## BDD Style

Gherkin `.feature` files live in `tests/features/` and are executed with `pytest-bdd`. Tests also use descriptive names that describe behavior, not implementation. Use `given/when/then` naming where it improves clarity:

```python
def test_session_start_requires_active_project():
    ...

def test_given_no_project_when_session_start_then_raises_no_active_project_error():
    ...
```

## Related Lode Files

- [patterns.md](patterns.md) — patterns being tested
- [../framework/rules.md](../framework/rules.md) — H-20 coverage requirement
