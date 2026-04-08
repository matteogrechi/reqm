---
id: ARCH-005
title: Export writes only to the user-specified output path
type: Constraint
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [architecture, safety, export]
relationships:
  derived_from: null
  related_to: [ARCH-004]
---

## Description

The tool shall write export output exclusively to the file path provided via `--output`; no files shall be written to any other location, including the requirements directory.

## Rationale

Limiting writes to one explicit, user-controlled path prevents unintended side effects, makes the tool's output deterministic, and supports audit trails.

## Acceptance Criteria

- The output file exists at the path given by `--output` after a successful export.
- No files are created or modified anywhere other than the `--output` path during an export run.
