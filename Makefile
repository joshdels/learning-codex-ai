.PHONY: run migrations migrate check test shell collectstatic

# Let uv load local environment variables without evaluating them as shell code.
ifneq ($(wildcard .env),)
export UV_ENV_FILE ?= .env
endif

run:
	uv run python manage.py runserver

migrations:
	uv run python manage.py makemigrations

migrate:
	uv run python manage.py migrate

check:
	uv run python manage.py check

test:
	uv run python manage.py test

shell:
	uv run python manage.py shell

collectstatic:
	uv run python manage.py collectstatic --noinput
