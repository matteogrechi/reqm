---
id: ARCH-009
title: Project metadata includes project_key field
type: Constraint
priority: High
status: Draft
stability: Volatile
verification: [Inspection]
tags: [architecture, metadata, project]
relationships:
  derived_from: [ARCH-008]
  related_to: [ARCH-010]
---

## Description

The `.project-metadata.md` file shall include a `project_key` field containing a string identifier for the project.

## Rationale

A short project identifier enables cross-project traceability and distinguishes requirements belonging to different projects within a shared repository.

## Acceptance Criteria

- The `project_key` field is accessible as a string value after parsing `.project-metadata.md`.
- When `project_key` is absent from the frontmatter, the parser returns an empty string.
