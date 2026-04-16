---
id: REQM-CLI-012
title: export command invokes the named exporter
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [cli, export]
relationships:
  derived_from: null
  related_to: [REQM-ARCH-001, REQM-ARCH-002, REQM-ARCH-003, REQM-CLI-013, REQM-CLI-014, REQM-CLI-015, REQM-CLI-020, REQM-EXP-001, REQM-EXP-006, REQM-EXP-010]
---

## Description

The `reqm export <name>` command shall invoke the exporter registered under `<name>` to produce the export artefact.

## Rationale

Export is the primary deliverable of reqm. A stable command interface decoupled from exporter implementation details allows the set of exporters to grow without breaking existing scripts or workflows.

## Acceptance Criteria

- `reqm export requirements` invokes the exporter registered as `requirements` and produces an output artefact.
