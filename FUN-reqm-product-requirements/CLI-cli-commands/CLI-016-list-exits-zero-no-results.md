---
id: CLI-016
title: list exits 0 when no requirements match
type: Functional
priority: Low
status: Draft
stability: Stable
verification: [Test]
tags: [cli, list]
relationships:
  derived_from: null
  related_to: [CLI-005]
---

## Description

The `reqm list` command shall exit with code 0 when no requirements match the applied filters.

## Rationale

A zero exit code for an empty result distinguishes "no match" from an error condition, preventing CI pipelines from treating an empty listing as a failure.

## Acceptance Criteria

- `reqm list --folder NONEXISTENT` exits with code 0.