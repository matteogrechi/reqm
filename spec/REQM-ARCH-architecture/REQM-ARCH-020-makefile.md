---
id: REQM-ARCH-020
title: Project shall provide a Makefile exposing standard developer commands
type: Functional
priority: Medium
status: Draft
stability: Stable
verification: [Inspection]
tags: [architecture, tooling, developer-experience]
relationships:
  derived_from: null
  related_to: [REQM-ARCH-019]
---

## Description

A `Makefile` at the project root shall expose the following standard developer
targets, all implemented using `uv` as the Python tool runner:

- `help` — print a concise list of available targets (default goal).
- `install-dev` — install the package and all development dependencies in editable mode.
- `test` — run the full test suite.
- `validate` — run `reqm validate` against the product requirements.
- `build` — produce a distributable wheel and sdist under `dist/`.
- `clean` — remove build artefacts (`dist/`, `*.egg-info`, `__pycache__`).

## Rationale

A Makefile provides a single, discoverable entry point for common developer tasks.
It reduces onboarding friction by eliminating the need to remember or look up
individual `uv run` invocations, and ensures all contributors use the same
command surface.

## Acceptance Criteria

- A file named `Makefile` exists at the project root.
- `make help` prints the list of available targets without error.
- `make install-dev` installs the package in editable mode with dev extras.
- `make test` invokes `uv run pytest` and exits with the same code.
- `make validate` invokes `uv run reqm validate` and exits with the same code.
- `make build` produces artefacts under `dist/`.
- `make clean` removes `dist/`, `*.egg-info`, and `__pycache__` directories.
