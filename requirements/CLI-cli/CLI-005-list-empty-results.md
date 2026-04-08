---
id: CLI-005
title: list prints a no-results message and exits 0 when no requirements match
type: Functional
priority: Low
status: Draft
stability: Stable
verification: [Test]
tags: [cli, list]
relationships:
  derived_from: null
  related_to: [CLI-001]
---

## Description

When no requirements match the applied filters, the `reqm list` command shall print a human-readable message indicating no results were found and exit with code 0.

## Rationale

An empty table with no explanation is ambiguous; an explicit message distinguishes "no match" from an error condition, preventing misinterpretation in automated pipelines.

## Acceptance Criteria

- `reqm list --folder NONEXISTENT` prints a non-empty "no results" message to stdout.
- The exit code is 0 when no requirements match.
