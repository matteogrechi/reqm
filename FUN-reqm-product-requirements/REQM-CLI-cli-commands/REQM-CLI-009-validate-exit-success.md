---
id: REQM-CLI-009
title: validate prints a success message when no errors are found
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [cli, validation]
relationships:
  derived_from: null
  related_to: [REQM-CLI-008, REQM-CLI-018]
---

## Description

The `reqm validate` command shall print a success message to stdout when no validation errors are found.

## Rationale

An explicit success message confirms to the user that validation ran and found nothing wrong, distinguishing a clean run from a silent failure.

## Acceptance Criteria

- `reqm validate` on a valid requirements set prints a non-empty success message to stdout.
