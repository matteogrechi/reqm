---
id: ARCH-013
title: ProjectMeta includes a validation_items_path field
type: Functional
priority: High
status: Draft
stability: Evolving
verification: [Test]
tags: [architecture, metadata, validation]
relationships:
  derived_from: [ARCH-008]
  related_to: [EXP-017]
---

## Description

The `ProjectMeta` dataclass shall include a `validation_items_path` field that stores the path to the folder containing validation item files, as declared in `.project-metadata.md`.

## Rationale

Decoupling the validation items folder location from the requirements root allows teams to organise their repository freely without hard-coding a path convention into the tool.

## Acceptance Criteria

- `ProjectMeta.validation_items_path` exists as a string field defaulting to `""`.
- When `.project-metadata.md` contains `validation_items_path: path/to/items`, the field is populated with that value after `load_project_meta` is called.
- When `validation_items_path` is absent from `.project-metadata.md`, the field defaults to `""`.