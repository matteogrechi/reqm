---
id: REQM-CLI-021
title: export exits 1 for unregistered exporter names
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [cli, export]
relationships:
  derived_from: null
  related_to: [REQM-CLI-014]
---

## Description

The `reqm export` command shall exit with code 1 when the specified exporter name is not registered.

## Rationale

A non-zero exit code allows scripts to detect when an export fails due to an unknown exporter, without requiring them to parse the error message.

## Acceptance Criteria

- `reqm export unknown-name` exits with code 1.