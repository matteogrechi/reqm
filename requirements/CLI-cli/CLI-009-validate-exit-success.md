---
id: CLI-009
title: validate exits 0 with a success message when no errors are found
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [cli, validation]
relationships:
  derived_from: null
  related_to: [CLI-008]
---

## Description

The `reqm validate` command shall print a success message to stdout and exit with code 0 when no validation errors are found.

## Rationale

A predictable zero exit code allows CI pipelines to gate builds and releases on a clean validation result.

## Acceptance Criteria

- `reqm validate` on a valid requirements set prints a success message to stdout.
- The exit code is 0 when all validation rules pass.
