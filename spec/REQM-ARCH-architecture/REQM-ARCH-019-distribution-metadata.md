---
id: REQM-ARCH-019
title: pyproject.toml shall declare complete distribution metadata for pip installation
type: Constraint
priority: Medium
status: Draft
stability: Stable
verification: [Inspection]
tags: [architecture, packaging, distribution]
relationships:
  derived_from: null
  related_to: [REQM-ARCH-020]
---

## Description

The `pyproject.toml` file shall declare all metadata fields required for a valid,
pip-installable Python package: `authors`, `readme`, `classifiers`, `keywords`,
and `[project.urls]`. These fields must be populated so that the package can be
built into a wheel and installed with `pip install` or `uv pip install` without
additional configuration.

## Rationale

A complete set of distribution metadata allows the package to be published to
PyPI and installed by end users without requiring access to the source tree.
It also communicates intent, licensing, and compatibility at a glance inside
package indexes and tooling.

## Acceptance Criteria

- `pyproject.toml` contains an `authors` entry with at least one name/email pair.
- `pyproject.toml` contains `readme = "README.md"`.
- `pyproject.toml` contains a non-empty `classifiers` list covering license,
  Python version, and at least one topic classifier.
- `pyproject.toml` contains a non-empty `keywords` list.
- `pyproject.toml` contains a `[project.urls]` table with at least a `Source` entry.
- `pip install .` (or `uv pip install .`) installs the `reqm` CLI successfully.
