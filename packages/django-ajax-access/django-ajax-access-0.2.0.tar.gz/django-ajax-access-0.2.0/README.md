# Django Ajax Access

## Description

A set of views and urls for ajax-based logout and logout for Django.

## Installation

```
pip install django_ajax_access
```

or

```
pipenv install django_ajax_access
```

## Usage

settings.py

```python
AJAX_ACCESS = {
  "LOGIN_RATELIMIT": {
    "KEY": "ip",
    "RATE": "10/h",
    "BLOCK": True,
  },
  "LOGOUT_RATELIMIT": {
    "KEY": "ip",
    "RATE": "10/h",
    "BLOCK": True,
  },
}
```

urls.py

```python
from django.conf.urls import url, include

urlpatterns = [
  ...
  url("^access/", include("ajax_access.urls")),
  ...
]
```
