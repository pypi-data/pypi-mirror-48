# flake8-todo-ticket

[![PyPI](https://img.shields.io/pypi/v/flake8-todo-ticket.svg)](https://pypi.python.org/pypi/flake8-todo-ticket)
[![PyPI](https://img.shields.io/pypi/pyversions/flake8-todo-ticket.svg)](https://pypi.python.org/pypi/flake8-todo-ticket)
[![codecov](https://codecov.io/gh/tommilligan/flake8-todo-ticket/branch/master/graph/badge.svg)](https://codecov.io/gh/tommilligan/flake8-todo-ticket/branch/master)
[![CircleCI branch](https://img.shields.io/circleci/project/github/tommilligan/flake8-todo-ticket/master.svg)](https://circleci.com/gh/tommilligan/flake8-todo-ticket)

Enforce ownership and ticketing of TODO notes.

This module provides a plugin for `flake8`, the Python code checker.

## Installation

Install with pip:

```bash
pip install flake8-todo-ticket
```

The plugin officially supports Python `>= 3.6` and `flake8 >= 3.7`.
You may find other Python 3 versions work as well.

## Usage

The plugin finds TODO comments without any indication as to why they exist.

```python
def my_function():
    # TODO
    # ^ who knows why this is here?
    pass
```

```log
./my_file.py:2:7: T400 Badly formatted TODO. Use TODO(name)[ticket_number]
```

To remove the error, add some basic information about this TODO:

```python
def my_function():
    # TODO(tommilligan)[2856]
    #      ^ who owns this temporary workaround
    #                   ^ ticket number for this issue
    pass
```

## Changelog

### 0.1.0

#### Features

- first commit, based on `flake8-fixme`
