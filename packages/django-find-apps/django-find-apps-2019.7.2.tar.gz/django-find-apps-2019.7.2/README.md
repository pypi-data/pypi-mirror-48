<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
https://pypi.org/project/django-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/django-find-apps.svg?longCache=True)](https://pypi.org/project/django-find-apps/)

#### Installation
```bash
$ [sudo] pip install django-find-apps
```

#### Commands
command|`help`
-|-
`python manage.py find_apps` |print list of project apps

#### Functions
function|`__doc__`
-|-
`django_find_apps.find_apps(path)` |return a list of apps

#### Examples
example #1:
```python
from django_find_apps import find_apps

INSTALLED_APPS = find_apps(".") + [
    ...
]
```

example #2:

settings:
```python
from django_find_apps import find_apps

PROJECT_APPS = open("apps.txt").read().splitlines()
INSTALLED_APPS = PROJECT_APPS + [
    "django_find_apps"
]
```

```bash
$ touch "apps.txt"
$ python manage.py find_apps > "apps.txt"
```

<p align="center">
    <a href="https://pypi.org/project/django-readme-generator/">django-readme-generator</a>
</p>