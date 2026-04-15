---
id: CLI-017
title: show exits 1 when the ID is not found
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [cli, show]
relationships:
  derived_from: null
  related_to: [CLI-007]
---

## Description

The `reqm show` command shall exit with code 1 when the given ID does not exist in the requirements collection.

## Rationale

A non-zero exit code allows scripts and CI pipelines to detect and handle a missing requirement programmatically, without parsing stderr output.

## Acceptance Criteria

- `reqm show UNKNOWN-999` exits with code 1.