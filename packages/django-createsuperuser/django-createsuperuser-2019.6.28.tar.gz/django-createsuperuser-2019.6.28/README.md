<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
https://pypi.org/project/django-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/django-createsuperuser.svg?longCache=True)](https://pypi.org/project/django-createsuperuser/)

#### Installation
```bash
$ [sudo] pip install django-createsuperuser
```

#### `settings.py`
```python
if DEBUG:
    INSTALLED_APPS = ["django_createsuperuser"]+INSTALLED_APPS
```

#### Commands
command|`help`
-|-
`python manage.py createsuperuser` |create/update a superuser with password

#### Examples
```bash
$ python manage.py createsuperuser --username admin --password admin
$ python manage.py createsuperuser --username admin --password admin --email 'admin@example.com'
```

<p align="center">
    <a href="https://pypi.org/project/django-readme-generator/">django-readme-generator</a>
</p>