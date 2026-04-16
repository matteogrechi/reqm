---
id: REQM-ARCH-016
title: Requirement IDs shall follow the format folder_id-NNN
type: Constraint
priority: High
status: Draft
stability: Evolving
verification: [Test]
tags: [architecture, ids, validation]
relationships:
  derived_from: null
  related_to: [REQM-ARCH-017, REQM-ARCH-008]
---

## Description

Every requirement ID shall be structured as `<folder_id>-<NNN>`, where `folder_id` is the `id` field of the enclosing folder's `.folder-metadata.md` and `NNN` is a zero-padded three-digit progressive number. Because folder IDs already embed the specification key (per REQM-ARCH-017), no separate specification key prefix is required in the requirement ID.

## Rationale

Deriving the requirement ID pattern purely from the folder ID eliminates redundancy: the specification key is already encoded in the folder ID (`REQM-ARCH`), so a requirement like `REQM-ARCH-001` is both globally unique and self-describing without repeating the specification key twice.

## Acceptance Criteria

- `reqm validate` emits an error for any requirement whose ID does not match the pattern `{folder_id}-\d{3}`.
- A requirement with ID `REQM-ARCH-001` in a folder with `id: REQM-ARCH` passes validation.
- A requirement with ID `ARCH-001` in a folder with `id: REQM-ARCH` fails validation.
