---
id: CLI-014
title: export exits 1 with an error message for unregistered exporter names
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [cli, export]
relationships:
  derived_from: null
  related_to: [CLI-012]
---

## Description

When the specified exporter name is not registered, the `reqm export` command shall print an error message and exit with code 1.

## Rationale

A clear error prevents silent no-ops when a user misspells an exporter name or references an exporter that has been removed, and allows scripts to detect the failure.

## Acceptance Criteria

- `reqm export unknown-name` prints an error message identifying the unknown exporter name.
- The exit code is 1 when the specified exporter is not registered.
