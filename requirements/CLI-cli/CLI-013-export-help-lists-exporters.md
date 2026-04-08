---
id: CLI-013
title: export --help lists all registered exporters
type: Functional
priority: Medium
status: Draft
stability: Stable
verification: [Test]
tags: [cli, export]
relationships:
  derived_from: null
  related_to: [CLI-012, ARCH-003]
---

## Description

The `reqm export --help` output shall list all currently registered exporters by name.

## Rationale

Discoverable subcommands eliminate the need for external documentation to identify available export formats, and make the tool self-describing.

## Acceptance Criteria

- `reqm export --help` includes the name of every exporter currently registered in `pyproject.toml`.
