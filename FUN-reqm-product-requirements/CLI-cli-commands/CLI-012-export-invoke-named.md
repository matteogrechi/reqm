---
id: CLI-012
title: export command invokes the named exporter
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [cli, export]
relationships:
  derived_from: null
  related_to: [ARCH-001, ARCH-002, ARCH-003, CLI-013, CLI-014, CLI-015, CLI-020, EXP-001, EXP-006, EXP-010]
---

## Description

The `reqm export <name>` command shall invoke the exporter registered under `<name>` to produce the export artefact.

## Rationale

Export is the primary deliverable of reqm. A stable command interface decoupled from exporter implementation details allows the set of exporters to grow without breaking existing scripts or workflows.

## Acceptance Criteria

- `reqm export requirements` invokes the exporter registered as `requirements` and produces an output artefact.
