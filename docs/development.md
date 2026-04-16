# Development

## Prerequisites

- Python ≥ 3.14
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Setup

```sh
make install-dev
```

This runs `uv sync --all-extras`, installing the package in editable mode
together with all development dependencies (`pytest`, `pytest-cov`).

## Makefile targets

| Target | Command | Description |
| --- | --- | --- |
| `make help` | — | List all available targets (default) |
| `make install-dev` | `uv sync --all-extras` | Install package + dev deps in editable mode |
| `make test` | `uv run pytest` | Run the full test suite |
| `make coverage` | `uv run pytest --cov=reqm --cov-report=term-missing` | Run tests with line-level coverage report |
| `make export` | `reqm export …` (all exporters) | Export all Excel reports into `exports/` |
| `make validate` | `uv run reqm validate` (in spec dir) | Validate the product requirements |
| `make build` | `uv build` | Build wheel and sdist into `dist/` |
| `make clean` | — | Remove `dist/`, `*.egg-info`, `__pycache__` |

## Building a distributable package

```sh
make build
```

Produces a wheel (`.whl`) and a source distribution (`.tar.gz`) under `dist/`.
These can be installed directly:

```sh
pip install dist/reqm-*.whl
```

## Running tests

```sh
make test
```

Individual test files live under `tests/`. All tests use `uv run pytest`.

## Coverage report

```sh
make coverage
```

Runs the test suite with `pytest-cov` and prints a per-file line coverage
summary, highlighting uncovered lines in the `Missing` column.

## Exporting reports

```sh
make export
```

Runs all three built-in exporters against the product requirements and writes
the results to `exports/` at the project root:

| File | Exporter |
| --- | --- |
| `exports/requirements.xlsx` | Flat requirements list |
| `exports/traceability.xlsx` | Parent → child traceability matrix |
| `exports/test-results.xlsx` | Validation plan and coverage report |

The `exports/` directory is created automatically if absent and is excluded
from git via `.gitignore`.

## Validating product requirements

```sh
make validate
```

Runs `reqm validate` against `spec/`, exiting non-zero
if any requirement violates the validation rules.
