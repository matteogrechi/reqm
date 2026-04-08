---
id: CLI-015
title: export --root option overrides the default requirements root
type: Functional
priority: Medium
status: Draft
stability: Stable
verification: [Test]
tags: [cli, export]
relationships:
  derived_from: null
  related_to: [CLI-012]
---

## Description

The `reqm export` command shall accept a `--root <path>` option that causes the exporter to read requirements from the specified directory instead of the default requirements root.

## Rationale

Consistent with other commands, `--root` enables export of requirements stored outside the default path, supporting multi-project setups.

## Acceptance Criteria

- `reqm export requirements --root <path>` exports requirements read from `<path>`.
- When `--root` is specified, no requirements are read from `requirements/`.
