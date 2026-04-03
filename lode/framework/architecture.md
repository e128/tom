# Architecture
*Updated: 2026-04-03T00:00:00Z*

Jerry uses hexagonal (ports and adapters) architecture with strict layer isolation enforced by H-07.

## Layer Structure

```mermaid
graph TD
    I[Interface Layer<br/>src/jerry/interface/] --> A
    A[Application Layer<br/>src/jerry/application/] --> D
    D[Domain Layer<br/>src/jerry/domain/] --> SK
    SK[Shared Kernel<br/>src/jerry/shared_kernel/]
    INFRA[Infrastructure Layer<br/>src/jerry/infrastructure/] --> D
    INFRA --> A
    CR[Composition Root<br/>src/jerry/bootstrap.py] --> INFRA
    CR --> I
```

## Import Rules (H-07)

| Layer | May Import |
|-------|-----------|
| domain | shared_kernel only |
| application | domain, shared_kernel |
| infrastructure | domain, application, shared_kernel, external libs |
| interface | application, shared_kernel |
| composition root | all layers |

## Key Directories

- `src/jerry/domain/` — entities, value objects, domain services, repository interfaces (ports)
- `src/jerry/application/` — use cases, command/query handlers
- `src/jerry/infrastructure/` — file-based adapters, external integrations
- `src/jerry/interface/` — CLI commands (Click/Typer)
- `src/jerry/session_management/` — session lifecycle
- `src/jerry/work_tracking/` — worktracker entity management
- `src/jerry/shared_kernel/` — shared primitives, exceptions, base types

## One Class Per File (H-10)

Each Python file contains exactly one public class. File names match class names (snake_case).

## Related Lode Files

- [rules.md](rules.md) — H-07 and other architecture HARD rules
- [../practices.md](../practices.md) — layer rules summary
