# Python Utilities

Collection of various, often reused Python utility functions.

All functions here are covered by tests.

This library has no other dependencies other than Python.

## Usage

Install:

```
pip install git+https://github.com/extrange/python-utils
```

Usage:

```
from python_utils import format_hhmmss

# Use functions as per normal
```

## Development Notes

[Install `uv`](https://docs.astral.sh/uv/getting-started/installation/), then activate the venv with `source .venv/bin/activate`.

Testing: `pytest --cov-report html --cov src`

When making **breaking changes** (e.g. removing functions and/or making parameters incompatible), update the major version number (i.e. 1.0.0 -> 2.0.0).

For compatible changes, (e.g. adding functions) update the minor version number (i.e. 1.0.0 -> 1.1.0).

For bugfixes, update the patch version (i.e. 1.0.0 -> 1.0.1).

For more information, refer to [Semver](https://semver.org/).

Running tests:
