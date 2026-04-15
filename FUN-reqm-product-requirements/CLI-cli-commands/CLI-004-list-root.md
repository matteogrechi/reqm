---
id: CLI-004
title: list --root option overrides default requirements root
type: Functional
priority: Medium
status: Draft
stability: Stable
verification: [Test]
tags: [cli, list]
relationships:
  derived_from: null
  related_to: [CLI-001]
---

## Description

The `reqm list` command shall accept a `--root <path>` option that overrides the default requirements root directory (default: `FUN-reqm-product-requirements/`).

## Rationale

Users may store requirements outside the default path; `--root` enables the tool to operate on any compliant directory without reconfiguration.

## Acceptance Criteria

- `reqm list --root <path>` discovers requirements under `<path>`.
- When `--root` is specified, no requirements are read from `FUN-reqm-product-requirements/`.
