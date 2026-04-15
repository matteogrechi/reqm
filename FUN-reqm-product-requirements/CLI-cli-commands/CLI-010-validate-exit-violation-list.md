---
id: CLI-010
title: validate prints each violation with its ID and rule when errors are found
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [cli, validation]
relationships:
  derived_from: null
  related_to: [CLI-008, CLI-019]
---

## Description

When one or more validation errors are found, the `reqm validate` command shall print each violation to stdout, including the requirement ID and the description of the rule that failed.

## Rationale

Individual violation messages with requirement IDs allow authors to locate and fix issues without manually examining all requirements files.

## Acceptance Criteria

- Given an invalid requirements set, `reqm validate` prints one line per violation.
- Each violation line includes the requirement ID and a description of the rule that failed.
