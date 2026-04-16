---
id: REQM-ARCH-010
title: Specification metadata includes related_specifications list
type: Constraint
priority: High
status: Draft
stability: Volatile
verification: [Inspection]
tags: [architecture, metadata, specification]
relationships:
  derived_from: [REQM-ARCH-008]
  related_to: [REQM-ARCH-009, REQM-ARCH-011]
---

## Description

The `.specification-metadata.md` file shall include a `related_specifications` field containing a list of entries, each with `id` and `local_path` attributes.

## Rationale

Declaring related specifications and their local paths enables cross-specification traceability links and validation item discovery without requiring hardcoded paths or manual configuration.

## Acceptance Criteria

- Each entry in `related_specifications` exposes `id` (string) and `local_path` (string) fields after parsing.
- When `related_specifications` is absent from the frontmatter, the parser returns an empty list.
