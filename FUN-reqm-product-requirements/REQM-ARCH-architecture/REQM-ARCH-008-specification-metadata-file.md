---
id: REQM-ARCH-008
title: Tool supports optional .specification-metadata.md file
type: Constraint
priority: High
status: Draft
stability: Volatile
verification: [Test]
tags: [architecture, metadata, specification]
relationships:
  derived_from: null
  related_to: [REQM-ARCH-009, REQM-ARCH-010, REQM-ARCH-011, REQM-ARCH-013, REQM-ARCH-014, REQM-ARCH-015]
---

## Description

The tool shall support an optional `.specification-metadata.md` file placed in the specification root directory containing YAML frontmatter with specification-level settings.

## Rationale

Users need a place to store specification-level metadata that applies to the entire requirements collection, separate from folder-level metadata (`.folder-metadata.md`). This enables cross-specification traceability by declaring related specifications and their local paths.

## Acceptance Criteria

- When `.specification-metadata.md` exists in the specification root, the tool discovers and parses it without error.
- When `.specification-metadata.md` is absent, the tool proceeds without error and does not raise an exception.
- When both `.specification-metadata.md` and `.project-metadata.md` exist in the same directory, the tool raises an error before loading any requirements.
