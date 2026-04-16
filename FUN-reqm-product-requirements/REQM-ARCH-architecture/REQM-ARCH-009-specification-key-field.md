---
id: REQM-ARCH-009
title: Specification metadata includes id, title, description, and type fields
type: Constraint
priority: High
status: Draft
stability: Volatile
verification: [Inspection]
tags: [architecture, metadata, specification]
relationships:
  derived_from: [REQM-ARCH-008]
  related_to: [REQM-ARCH-010, REQM-ARCH-018]
---

## Description

The `.specification-metadata.md` file shall include:

- `id`: a string identifier for the specification.
- `title`: a human-readable name (optional).
- `description`: descriptive text drawn from the `## Description` body section (optional).
- `type`: a string declaring the content of the specification directory. Allowed values are `requirements` (default) and `validation_items`.

Together with `related_specifications`, these fields make the specification metadata structure uniform with folder metadata and enable content-type-aware discovery.

## Rationale

A `type` field lets the tool distinguish between requirements specifications and validation items specifications without inspecting individual files. This enables `_load_items` to selectively load only the related specs declared as `validation_items`, and prevents requirements specs from being mistakenly treated as validation item sources.

## Acceptance Criteria

- The `id`, `title`, and `type` fields are accessible as string values after parsing `.specification-metadata.md`.
- The `description` field is populated from the `## Description` body section.
- When `type` is absent from the frontmatter, the parser returns `"requirements"`.
- When `id` or `title` is absent from the frontmatter, the parser returns an empty string for that field.
- When no `## Description` section is present in the body, `description` returns an empty string.
