# Django Applications

These instructions apply to `apps/` and its descendants, in addition to the root
`AGENTS.md`.

## Layout

Place all project-owned Django applications under `apps/`. The existing app is:

```text
apps/
    __init__.py
    website/
        apps.py
        urls.py
        views.py
        tests.py
        templates/
            website/
        static/
            website/
```

This illustrates app organization, not a requirement to create unused files.
The shared `base.html` currently lives in `apps/website/templates/`; follow the
root instructions when a task includes moving shared frontend files.

## App Configuration

- Use the full Python package path in `AppConfig.name`, such as `apps.website`.
- Register the app configuration in `INSTALLED_APPS`, such as
  `apps.website.apps.WebsiteConfig`.
- Include app URLs from `config/urls.py` using their full package path, such as
  `apps.website.urls`.
- Preserve app labels and URL namespaces unless explicitly asked to change them.

## Refactoring

New apps must follow this layout. Move or restructure existing apps only within
the requested scope.

When moving an app, update its configuration, registration, imports, and URL
includes. Check for references in tests and documentation as well.

Verify page rendering, named URL resolution, template discovery, and static-file
discovery after relocation. Follow the root testing and workflow requirements.
