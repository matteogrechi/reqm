---
id: CLI-001
title: list command recursively discovers requirement files
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [cli, list]
relationships:
  derived_from: null
  related_to: [CLI-002, CLI-003, CLI-004, CLI-005]
---

## Description

The `reqm list` command shall recursively discover all requirement files under the requirements root.

## Rationale

Requirements may be organised in nested subdirectories; recursive discovery ensures no requirement is silently omitted from the listing.

## Acceptance Criteria

- `reqm list` returns an entry for every requirement file present at any subdirectory depth under the requirements root.
