<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/import-env-file.svg?longCache=True)](https://pypi.org/project/import-env-file/)

#### Installation
```bash
$ [sudo] pip install import-env-file
```

#### Examples
`.env`
```python
DB_NAME="name"
...
```

`settings.py`
```python
import import_env_file
import os

DATABASES = {
    'default': {
        'NAME': os.getenv('DB_NAME'),
    }
}
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>