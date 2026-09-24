# Django Configuration

These instructions apply to `config/` and its descendants, in addition to the
root `AGENTS.md`.

This directory contains settings, root URLs, and WSGI/ASGI entry points. Keep
project-owned Django apps under `apps/`.

## Settings Layout

- Keep shared settings in `config/settings/base.py`.
- Keep development settings in `config/settings/local.py`.
- Keep production settings in `config/settings/prod.py`.
- Import shared settings from `base.py` in both environment modules.
- Keep `config/settings/__init__.py` free of environment selection logic.

Use the existing `prod.py` name consistently in code and documentation. Rename
settings modules only when the task explicitly includes that change.

## Environment Selection

- Default management commands to `config.settings.local`.
- Default WSGI/ASGI entry points to `config.settings.prod`.
- Respect an explicitly supplied `DJANGO_SETTINGS_MODULE`; use
  `os.environ.setdefault` for entry-point defaults.
- Enable debug mode locally and disable it in production.

## Secrets and Environment Variables

- Read secrets from environment variables. Never hard-code secrets or provide
  production secret defaults.
- Keep `.env` ignored by Git and avoid exposing secret values in logs or output.
- Makefile commands load the root `.env` through uv when present. Python settings
  modules do not load `.env` themselves.
- For direct Django commands with a `.env` file, use
  `uv run --env-file .env python manage.py <command>`.
- Supply production environment variables through the deployment environment.
- Read production allowed hosts from `DJANGO_ALLOWED_HOSTS`.

## Production Static Files

Keep WhiteNoise configuration in `prod.py`, with its middleware immediately after
Django's security middleware. Use the compressed manifest static-file storage
backend and collect assets into `STATIC_ROOT` before starting production.

Preserve local static-file handling when changing production settings.
