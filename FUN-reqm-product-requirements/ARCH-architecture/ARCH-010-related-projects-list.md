---
id: ARCH-010
title: Project metadata includes related_projects list
type: Constraint
priority: High
status: Draft
stability: Volatile
verification: [Inspection]
tags: [architecture, metadata, project]
relationships:
  derived_from: [ARCH-008]
  related_to: [ARCH-009, ARCH-011]
---

## Description

The `.project-metadata.md` file shall include a `related_projects` field containing a list of entries, each with `id`, `title`, and `local_path` attributes.

## Rationale

Declaring related projects and their local paths enables cross-project traceability links without requiring hardcoded paths or manual configuration.

## Acceptance Criteria

- Each entry in `related_projects` exposes `id` (string), `title` (string), and `local_path` (string) fields after parsing.
- When `related_projects` is absent from the frontmatter, the parser returns an empty list.
