# Project Instructions

## Project and Stack

TopMap Solutions is a Django monolith using Python, uv, Django templates, HTML,
and CSS. Prefer simple implementations and Django built-in features.

## Instruction Scope

This file contains project-wide rules. Read applicable nested `AGENTS.md` files
before editing files in their directories. Keep directory-specific rules in those
nested files rather than duplicating the project-wide workflow.

## Architecture

Keep project configuration in `config/` and project-owned Django apps in `apps/`.
The current layout is:

```text
config/
    settings/
        __init__.py
        base.py
        local.py
        prod.py
    urls.py
    wsgi.py
    asgi.py
apps/
    __init__.py
    website/
```

Place future apps under `apps/` only when requested. Do not create placeholder
apps or move existing files outside the requested scope.

## Frontend

The intended layout for shared frontend files is:

```text
templates/
    base.html
    components/
static/
    css/
    js/
    images/
```

The shared base template and stylesheet currently live inside `apps/website/`.
Move them to the intended layout only when the task includes that refactor.
Create directories only when they have content.

Keep app-specific templates and static assets namespaced inside their apps.
Reuse the shared base template. Do not add JavaScript frameworks unless requested.

## Django Rules

- Keep views thin and business logic out of templates.
- Use named URLs and app namespaces.
- Avoid unnecessary abstractions and dependencies.
- Do not introduce APIs unless requested.
- Preserve existing behavior unless the requested change requires otherwise.

## Developer Commands

Maintain a simple root `Makefile`. Use uv for Python dependency management and
for running Python and Django commands. Prefer these Makefile targets:

| Target | Command |
| --- | --- |
| `make run` | `uv run python manage.py runserver` |
| `make migrations` | `uv run python manage.py makemigrations` |
| `make migrate` | `uv run python manage.py migrate` |
| `make check` | `uv run python manage.py check` |
| `make test` | `uv run python manage.py test` |
| `make shell` | `uv run python manage.py shell` |
| `make collectstatic` | `uv run python manage.py collectstatic --noinput` |

Makefile commands load the root `.env` through uv when the file exists. Keep
existing exported environment variables authoritative. Add targets only when
useful to the current project.

## Testing

Each app should contain meaningful tests for its behavior. Add or update tests
when appropriate for the change.

After code or configuration changes, run:

```sh
make check
make test
```

Do not consider a task complete if relevant tests fail. Report failures and state
when no tests were discovered. For documentation-only changes, verify accuracy,
consistency, and formatting; Django checks and tests are not required.

## Documentation

Update `README.md` when setup instructions, architecture, developer commands, or
dependencies change. Keep documented paths and settings module names consistent
with the implementation.

## Workflow

1. Read this file and applicable nested instructions.
2. Inspect the relevant existing files.
3. Explain the implementation plan before modifying files.
4. Make the smallest reasonable change within the requested scope.
5. Run the relevant checks and tests.
6. Summarize changes, validation results, and any remaining limitations.

## Definition of Done

- The implementation matches the requested scope.
- Existing behavior is preserved unless a change was requested.
- Required checks and relevant tests pass.
- No unrelated files are changed.
- Documentation is updated when necessary.
