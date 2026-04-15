---
id: CLI-019
title: validate exits 1 when validation errors are found
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [cli, validation]
relationships:
  derived_from: null
  related_to: [CLI-010]
---

## Description

The `reqm validate` command shall exit with code 1 when one or more validation errors are found.

## Rationale

A non-zero exit code enables CI pipelines to block builds and releases on an invalid requirements set, without requiring them to parse the violation output.

## Acceptance Criteria

- `reqm validate` on an invalid requirements set exits with code 1.