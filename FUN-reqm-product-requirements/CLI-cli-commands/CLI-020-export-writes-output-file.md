---
id: CLI-020
title: export writes artefact to the --output path
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [cli, export]
relationships:
  derived_from: null
  related_to: [CLI-012, ARCH-005]
---

## Description

The `reqm export <name>` command shall write the export artefact to the file path specified by `--output`, defaulting to `<name>.xlsx` in the current directory when `--output` is omitted.

## Rationale

An explicit, user-controlled output path makes the tool deterministic and safe; defaulting to `<name>.xlsx` reduces friction for interactive use without requiring an explicit flag every time.

## Acceptance Criteria

- `reqm export requirements -o report.xlsx` produces a file at `report.xlsx`.
- When `--output` is omitted, the output file is written to `requirements.xlsx` in the current directory.