# Katan AI

Table of contents:

- [Installation](#Installation)
- [Guide](#Guide)
- [Developement](#Developement)

# Installation
requires python 3.8
```bash
pip install poetry
poetry install
#TODO
```

# Guide

<!-- Subsection explaining how to use package -->

# Developement
To develop, install dependencies and enable pre-commit hooks.


```bash
pip install -U pip
pip install poetry pre-commit
poetry install
pre-commit install -t pre-commit -t pre-push
```

To run tests:

```bash
poetry run pytest
```
