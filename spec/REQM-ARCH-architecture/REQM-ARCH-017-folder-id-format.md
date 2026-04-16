---
id: REQM-ARCH-017
title: Folder IDs shall follow the format specification_key-folder_key
type: Constraint
priority: High
status: Draft
stability: Evolving
verification: [Inspection]
tags: [architecture, metadata, ids]
relationships:
  derived_from: [REQM-ARCH-009]
  related_to: [REQM-ARCH-016, REQM-ARCH-008]
---

## Description

The `id` field in each `.folder-metadata.md` file shall follow the format `<specification_key>-<folder_key>`, where `specification_key` matches the value declared in `.specification-metadata.md` and `folder_key` is a short uppercase identifier for the folder. The folder directory name shall follow the corresponding pattern `<specification_key>-<folder_key>-<slug>`.

## Rationale

Embedding the specification key in the folder ID ensures that folder IDs are globally unique across specifications and directly derivable from the folder directory name. This alignment with the requirement ID convention (`<folder_id>-NNN`) makes the ID structure consistent and self-documenting at every level.

## Acceptance Criteria

- Each `.folder-metadata.md` `id` field is of the form `<specification_key>-<folder_key>` (e.g., `REQM-ARCH`).
- The parent directory name of the `.folder-metadata.md` file begins with the same `<specification_key>-<folder_key>` prefix (e.g., `REQM-ARCH-architecture/`).
