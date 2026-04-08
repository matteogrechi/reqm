---
id: CLI-007
title: show exits 1 with an error message when the ID is not found
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [cli, show]
relationships:
  derived_from: null
  related_to: [CLI-006]
---

## Description

When the given ID does not exist in the requirements collection, the `reqm show` command shall print an error message to stderr and exit with code 1.

## Rationale

A non-zero exit code allows scripts and CI pipelines to detect and handle missing requirements programmatically; stderr output keeps the error separate from normal output.

## Acceptance Criteria

- `reqm show UNKNOWN-999` prints an error message to stderr.
- The exit code is 1 when the given ID is not found.
