---
id: REQM-CLI-007
title: show prints an error to stderr when the ID is not found
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [cli, show]
relationships:
  derived_from: null
  related_to: [REQM-CLI-006, REQM-CLI-017]
---

## Description

When the given ID does not exist in the requirements collection, the `reqm show` command shall print an error message to stderr.

## Rationale

Writing the error to stderr keeps it separate from normal stdout output, allowing scripts and CI pipelines to distinguish error messages from valid requirement content.

## Acceptance Criteria

- `reqm show UNKNOWN-999` prints a non-empty error message to stderr.
