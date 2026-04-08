---
id: CLI-002
title: list command prints a summary table to stdout
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [cli, list]
relationships:
  derived_from: null
  related_to: [CLI-001]
---

## Description

The `reqm list` command shall print a table to stdout containing one row per discovered requirement with columns: ID, Title, Type, Verification Method, and Folder ID.

## Rationale

A concise tabular overview is the most frequent daily interaction with a requirements set; it lets authors scan what exists and triage by type or folder without opening individual files.

## Acceptance Criteria

- The output table contains exactly the columns ID, Title, Type, Verification Method, and Folder ID.
- Each discovered requirement occupies exactly one row.
