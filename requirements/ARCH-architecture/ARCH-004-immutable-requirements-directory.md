---
id: ARCH-004
title: Requirements directory is immutable to the tool
type: Constraint
priority: Critical
status: Draft
stability: Locked
verification: [Test]
tags: [architecture, safety]
relationships:
  derived_from: null
  related_to: [ARCH-005, ARCH-006]
---

## Description

The tool shall not create, modify, or delete any file inside the requirements directory tree under any operating condition.

## Rationale

Requirements are source-controlled documents owned by the user. Accidental writes would corrupt version history and undermine the git-native versioning model defined in ARCH-006.

## Acceptance Criteria

- After executing any `reqm` command, all files under the requirements root are bit-for-bit identical to their state before the command was run.
- No temporary or intermediate files are created inside the requirements directory tree.
