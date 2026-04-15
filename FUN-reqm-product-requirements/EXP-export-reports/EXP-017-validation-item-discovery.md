---
id: EXP-017
title: Tool discovers validation items from the path declared in project metadata
type: Functional
priority: High
status: Draft
stability: Evolving
verification: [Test]
tags: [validation, discovery, metadata]
relationships:
  derived_from: [ARCH-013]
  related_to: [EXP-016, EXP-013]
---

## Description

The tool shall discover validation item files by recursively scanning the directory identified by `ProjectMeta.validation_items_path`. When `validation_items_path` is empty, the tool shall skip validation item loading without error.

## Rationale

Reading the validation items root from project metadata keeps the filesystem layout configurable per repository and avoids hard-coding a path convention in the tool binary.

## Acceptance Criteria

- When `validation_items_path` is set and the directory exists, all `.md` files with YAML frontmatter under that path are loaded as `ValidationItem` objects.
- When `validation_items_path` is empty, no validation items are loaded and no error is raised.