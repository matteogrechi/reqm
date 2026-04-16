---
id: REQM-ARCH-018
title: Validation items collections shall be structured as specifications
type: Constraint
priority: High
status: Draft
stability: Evolving
verification: [Inspection]
tags: [architecture, metadata, validation]
relationships:
  derived_from: [REQM-ARCH-008]
  related_to: [REQM-ARCH-009, REQM-ARCH-013, REQM-EXP-016]
---

## Description

A validation items collection shall be a directory structured identically to a requirements specification: it shall contain a `.specification-metadata.md` file at its root declaring `type: validation_items`, and may contain `.folder-metadata.md` subfolders for organisational grouping. The only difference from a requirements specification is the frontmatter schema of the individual files it contains.

## Rationale

Treating validation items as a specification unifies the structural model. Both requirements and validation items collections share the same root discovery mechanism, the same subfolder organisation pattern, and the same metadata files. Tool code that discovers and loads content from either type of specification uses the same filesystem traversal; only the parser differs.

## Acceptance Criteria

- A validation items specification root contains a `.specification-metadata.md` file with `type: validation_items`.
- The directory may contain `.folder-metadata.md` files in subfolders; these are skipped by `load_validation_items`.
- `load_validation_items` returns only `ValidationItem` objects from files in the directory, ignoring all dotfiles and files without YAML frontmatter.
