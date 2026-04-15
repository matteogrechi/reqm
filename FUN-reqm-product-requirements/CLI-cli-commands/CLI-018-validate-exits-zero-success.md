---
id: CLI-018
title: validate exits 0 when no errors are found
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [cli, validation]
relationships:
  derived_from: null
  related_to: [CLI-009]
---

## Description

The `reqm validate` command shall exit with code 0 when no validation errors are found.

## Rationale

A predictable zero exit code allows CI pipelines to gate builds and releases on a clean validation result without parsing command output.

## Acceptance Criteria

- `reqm validate` on a valid requirements set exits with code 0.