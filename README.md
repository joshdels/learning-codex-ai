# TopMap Solutions

A minimal Django website with a homepage (`/`) and About page (`/about/`).
Both pages share a base template and a small CSS stylesheet.

## Local development

Install Python 3.14 or newer, `uv`, and `make`, then run:

```sh
uv sync
export DJANGO_SECRET_KEY="$(uv run python -c 'import secrets; print(secrets.token_urlsafe(50))')"
make run
```

Open http://127.0.0.1:8000/ in your browser.
No database setup or migrations are required.

Alternatively, save `DJANGO_SECRET_KEY` in a root `.env` file instead of exporting
it for each terminal session. Makefile commands automatically load this file:

```dotenv
DJANGO_SECRET_KEY='your-generated-secret-key'
```

Use single quotes to preserve special characters literally. `.env` is ignored by Git.

## Developer Commands

Run these commands from the project root. All targets use `uv` to run Django.

| Command | Purpose |
| --- | --- |
| `make run` | Start the development server. |
| `make migrations` | Generate database migrations. |
| `make migrate` | Apply database migrations. |
| `make check` | Run Django system checks. |
| `make test` | Run Django tests. |
| `make shell` | Open the Django Python shell. |
| `make collectstatic` | Collect static files with `--noinput`. |

Run `make check` and `make test` after changes. Database commands require a
configured database; run `make collectstatic` with production settings.

## Selecting settings

- `config.settings.base` contains shared settings.
- `config.settings.local` enables debug mode and is the default for `manage.py`
  and Makefile commands.
- `config.settings.prod` disables debug mode and is the default for WSGI/ASGI.
  It uses WhiteNoise to serve collected, compressed static files.

Set `DJANGO_SECRET_KEY` in your environment for both local and production use.
The local setup command above generates a temporary development key. In
production, configure a persistent secret through your deployment environment.
Makefile commands load the root `.env` when present; existing exported variables
take precedence. For direct Django commands, use
`uv run --env-file .env python manage.py <command>`. WSGI/ASGI servers need
environment variables supplied by their deployment environment.

To select production settings explicitly:

```sh
export DJANGO_SETTINGS_MODULE=config.settings.prod
export DJANGO_ALLOWED_HOSTS=example.com,www.example.com
make check
make collectstatic
```

Replace the example hosts with your actual domains. Collect static files before
starting your production server. To switch back to local development:

```sh
export DJANGO_SETTINGS_MODULE=config.settings.local
make run
```

## Structure

- `config/`: Project URLs and WSGI/ASGI entry points.
- `config/settings/`: Shared, local, and production settings.
- `website/`: Page views, URLs, templates, and static CSS.
- `website/templates/base.html`: Shared page layout and navigation.
