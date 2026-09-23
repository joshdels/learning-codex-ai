# AGENTS.md

## Project

TopMap Solutions Django website.

## Stack

- Python
- Django
- uv
- Django Templates
- HTML/CSS

## Architecture

Use a Django monolith.

Project configuration:

    config/
        settings/
            base.py
            local.py
            production.py
        urls.py
        wsgi.py
        asgi.py

Django applications live inside:

    apps/

Example:

    apps/
        website/
        accounts/

## Frontend

Global frontend assets live in:

    static/
        css/
        js/
        images/

Shared templates live in:

    templates/
        base.html
        components/

App-specific templates may live inside their apps.

## Django Rules

- Keep views thin.
- Keep business logic out of templates.
- Prefer Django built-ins.
- Use named URLs.
- Use app namespaces.
- Do not introduce APIs unless requested.
- Do not introduce JavaScript frameworks unless requested.

## Settings

Shared settings belong in:

    config/settings/base.py

Development-only settings belong in:

    config/settings/local.py

Production-only settings belong in:

    config/settings/production.py

Secrets must come from environment variables.

Never hard-code secrets.

## Developer Commands

Create and maintain a root-level `Makefile` for common development commands.

Use `uv` to run Python and Django commands.

The Makefile should provide these commands:

    make run
    make migrations
    make migrate
    make check
    make test
    make shell
    make collectstatic

The commands should map to:

    make run
    -> uv run python manage.py runserver

    make migrations
    -> uv run python manage.py makemigrations

    make migrate
    -> uv run python manage.py migrate

    make check
    -> uv run python manage.py check

    make test
    -> uv run python manage.py test

    make shell
    -> uv run python manage.py shell

    make collectstatic
    -> uv run python manage.py collectstatic --noinput

Prefer Makefile commands when running common development tasks.

Keep the Makefile simple.
Do not add commands unless they are useful to the current project.

## Testing

Each app should contain tests.

Before completing a task run:

    make check
    make test

Add tests for new behavior when appropriate.

Do not consider a task complete if relevant tests fail.

## Documentation

Update README.md when:

- setup instructions change
- architecture changes
- developer commands change
- dependencies change

Document important Makefile commands in README.md.

## Workflow

Before modifying code:

1. Read this file.
2. Inspect relevant existing files.
3. Explain the implementation plan.
4. Make the smallest reasonable change.
5. Run relevant checks/tests.
6. Summarize the changes.

## Definition of Done

A task is complete only when:

- implementation matches the requested scope
- existing behavior is preserved
- `make check` passes
- relevant tests pass
- no unrelated files are changed
- documentation is updated when necessary
