---
id: CLI-010
title: validate exits 1 and lists each violation when errors are found
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

When one or more validation errors are found, the `reqm validate` command shall print each violation to stdout — including the requirement ID and a human-readable description of the violation — and exit with code 1.

## Rationale

Individual violation messages with IDs allow authors to locate and fix issues without manually examining all requirements. A non-zero exit code enables CI pipelines to block on invalid requirements.

## Acceptance Criteria

- Given an invalid requirements set, `reqm validate` prints one line per violation.
- Each violation line includes the requirement ID and a description of the rule that failed.
- The exit code is 1 when at least one validation error is found.
