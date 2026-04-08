---
id: ARCH-006
title: Version control delegated entirely to git
type: Constraint
priority: High
status: Draft
stability: Locked
verification: [Inspection]
tags: [architecture, git, versioning]
relationships:
  derived_from: null
  related_to: [ARCH-004, ARCH-007]
---

## Description

All versioning, history, diffing, and baselining of requirements shall be delegated entirely to git; the tool shall not provide any equivalent capability.

## Rationale

Reimplementing version control duplicates well-established git functionality, adds maintenance burden, and creates two competing sources of truth. Storing requirements as plain `.md` files makes them natively compatible with all git tooling without any special support from reqm.

## Acceptance Criteria

- Requirements can be diffed, branched, and tagged using standard git commands with no involvement from reqm.
- The `reqm` codebase contains no module that reads from or writes to a git repository on behalf of the user.
