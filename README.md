# PyPI Package Project Template

![GitHub License](https://img.shields.io/github/license/rexzhang/python-project-template)
![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/rexzhang/python-project-template/main/pyproject.toml)
[![PyPI - Version](https://img.shields.io/pypi/v/example)](https://pypi.org/project/example/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/django-light-auth)](https://pypi.org/project/example/)

## Check with pytest

### GihHub's `Actions secrets`

setup: `CODECOV_TOKEN`

## Release Docker

### GihHub's `Actions variables`

setup: `DOCKERHUB_REPOSITORY`,  eg: `ray1ex/asgi-webdav`

### GihHub's `Actions secrets`

setup: `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN`

### Ref

- <https://packaging.python.org/guides/distributing-packages-using-setuptools>
- <https://packaging.python.org/en/latest/distributing.html>
- <https://github.com/pypa/sampleproject>

## Release PyPI

### GihHub's `Environments`

Create a new environment: `pypi`

setup: `PYPI_PROJECT_URL`
