---
id: REQM-ARCH-006
title: Version control delegated entirely to git
type: Constraint
priority: High
status: Draft
stability: Locked
verification: [Inspection]
tags: [architecture, git, versioning]
relationships:
  derived_from: null
  related_to: [REQM-ARCH-004, REQM-ARCH-007]
---

## Description

The tool shall rely exclusively on git for all versioning, history, diffing, and baselining of requirements, providing no equivalent internal capability.

## Rationale

Reimplementing version control duplicates well-established git functionality, adds maintenance burden, and creates two competing sources of truth. Storing requirements as plain `.md` files makes them natively compatible with all git tooling without any special support from reqm.

## Acceptance Criteria

- Requirements can be diffed and branched using standard git commands without invoking any `reqm` command.
- Requirements can be tagged using standard git commands without invoking any `reqm` command.
- The `reqm` codebase contains no module that reads from or writes to a git repository on behalf of the user.
