---
id: REQM-CLI-011
title: validate --root option overrides the default requirements root
type: Functional
priority: Medium
status: Superseded
stability: Stable
verification: [Test]
tags: [cli, validation]
relationships:
  derived_from: null
  related_to: [REQM-CLI-008]
---

## Description

The `reqm validate` command shall accept a `--root <path>` option that causes validation to run against the specified directory instead of the default requirements root.

## Rationale

Consistent with other commands, `--root` enables validation of requirements stored outside the default path, supporting multi-project setups.

## Acceptance Criteria

- `reqm validate --root <path>` validates requirements found under `<path>`.
- When `--root` is specified, no requirements are read from `spec/`.
