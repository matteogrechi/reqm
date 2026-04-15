---
id: CLI-014
title: export prints an error message for unregistered exporter names
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [cli, export]
relationships:
  derived_from: null
  related_to: [CLI-012, CLI-021]
---

## Description

When the specified exporter name is not registered, the `reqm export` command shall print an error message identifying the unknown name.

## Rationale

A clear error prevents silent no-ops when a user misspells an exporter name or references an exporter that has been removed.

## Acceptance Criteria

- `reqm export unknown-name` prints an error message that includes the unrecognised exporter name.
