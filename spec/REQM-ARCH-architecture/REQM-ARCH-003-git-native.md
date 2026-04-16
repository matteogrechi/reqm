---
id: REQM-ARCH-003
title: Runtime exporter discovery by the CLI
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [architecture, export, plugins]
relationships:
  derived_from: null
  related_to: [REQM-ARCH-001, REQM-ARCH-002]
---

## Description

The CLI shall discover all registered exporters at runtime and expose each one as a named subcommand of `reqm export`, with no exporter name hard-coded in the CLI source.

## Rationale

Runtime discovery decouples the CLI from the set of available exporters, so adding or removing exporters requires no changes to CLI code and no redeployment of the core tool.

## Acceptance Criteria

- `reqm export --help` lists every exporter currently registered in `pyproject.toml`.
- No exporter name appears as a literal string in `cli.py`.
