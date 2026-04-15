---
id: ARCH-008
title: Tool supports optional .project-metadata.md file
type: Constraint
priority: High
status: Draft
stability: Volatile
verification: [Test]
tags: [architecture, metadata, project]
relationships:
  derived_from: null
  related_to: [ARCH-009, ARCH-010, ARCH-011, ARCH-013]
---

## Description

The tool shall support an optional `.project-metadata.md` file placed in the project root directory containing YAML frontmatter with project-level settings.

## Rationale

Users need a place to store project-level metadata that applies to the entire requirements collection, separate from folder-level metadata (`.folder-metadata.md`). This enables cross-project traceability by declaring related projects and their local paths.

## Acceptance Criteria

- When `.project-metadata.md` exists in the project root, the tool discovers and parses it without error.
- When `.project-metadata.md` is absent, the tool proceeds without error and does not raise an exception.
