---
id: REQM-ARCH-007
title: No internal versioning mechanism in the tool
type: Constraint
priority: High
status: Draft
stability: Locked
verification: [Inspection]
tags: [architecture, git, versioning]
relationships:
  derived_from: null
  related_to: [REQM-ARCH-006]
---

## Description

The tool shall contain no code for tracking revisions, snapshots, change history, or diffs of requirement content.

## Rationale

Keeping the tool free of internal versioning logic eliminates the risk of divergence from git history, reduces codebase size, and removes a class of maintenance burden entirely.

## Acceptance Criteria

- The codebase contains no module, class, or function that stores, compares, or retrieves previous versions of requirement content.
- No database, file, or in-memory structure is used to record the history of requirement changes.
