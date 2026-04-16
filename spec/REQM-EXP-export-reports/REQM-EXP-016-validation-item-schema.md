---
id: REQM-EXP-016
title: Validation item files use a defined frontmatter schema
type: Functional
priority: High
status: Draft
stability: Evolving
verification: [Inspection]
tags: [validation, schema, ecss]
relationships:
  derived_from: null
  related_to: [REQM-EXP-017, REQM-EXP-013]
---

## Description

Each validation item file shall be a Markdown file with YAML frontmatter containing the fields `id`, `title`, `method`, `level`, `status`, `priority`, `stability`, and optionally `tags`, `relationships.derived_from`, and `relationships.related_to`. The body shall support sections `## Objective`, `## Preconditions`, `## Procedure`, and `## Pass Criteria`.

## Rationale

A well-defined schema for validation items ensures consistent, machine-readable definitions of verification activities aligned with ECSS-E-ST-10-02C and IEEE 829, without capturing execution results which are managed by external systems.

## Acceptance Criteria

- A validation item file parsed by `parse_validation_item` exposes `id`, `title`, `method`, and `level` from frontmatter.
- Body sections `Objective`, `Preconditions`, `Procedure`, and `Pass Criteria` are extracted and accessible as named fields on the `ValidationItem` dataclass.
- Unrecognised frontmatter keys are silently ignored and do not raise a parse error.
