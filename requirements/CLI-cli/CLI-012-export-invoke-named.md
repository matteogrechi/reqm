---
id: CLI-012
title: export command invokes the named exporter and writes to --output
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [cli, export]
relationships:
  derived_from: null
  related_to: [ARCH-001, ARCH-002, ARCH-003, CLI-013, CLI-014, CLI-015, EXP-001, EXP-006, EXP-010]
---

## Description

The `reqm export <name>` command shall invoke the exporter registered under `<name>` and write the output to the file path specified by `--output` (default: `<name>.xlsx`).

## Rationale

Export is the primary deliverable of reqm. A stable command interface decoupled from exporter implementation details allows the set of exporters to grow without breaking existing scripts or workflows.

## Acceptance Criteria

- `reqm export requirements -o report.xlsx` produces an output file at `report.xlsx`.
- When `--output` is omitted, the output file is written to `<name>.xlsx` in the current directory.
