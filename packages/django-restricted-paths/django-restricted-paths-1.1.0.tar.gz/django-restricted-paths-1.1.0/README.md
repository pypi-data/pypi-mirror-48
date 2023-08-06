# Restricted Paths

## Description

Restricts access to specific urls based on DEBUG status by responded with a specific view or raising a 404.

## Installation

```python
pip install django-restricted-paths
```

## Usage

in settings.py:

```python
RESTRICTED_PATHS = {
  "PATHS": ("/admin",),
  "VIEW": "path.to.view.class.ViewClass",
}

MIDDLEWARE = (
    ...
    "restricted_paths.middleware.RestrictedPathsMiddleware"
)
```
