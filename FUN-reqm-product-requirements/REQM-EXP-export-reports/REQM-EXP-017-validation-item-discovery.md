---
id: REQM-EXP-017
title: Tool discovers validation items from related_specifications entries
type: Functional
priority: High
status: Draft
stability: Evolving
verification: [Test]
tags: [validation, discovery, metadata]
relationships:
  derived_from: [REQM-ARCH-013]
  related_to: [REQM-EXP-016, REQM-EXP-013]
---

## Description

The tool shall discover validation item files by recursively scanning the `local_path` directory of each entry in `related_specifications`. When an entry's `local_path` is empty or the directory does not exist, the tool shall skip that entry without error.

## Rationale

Tying validation item discovery to `related_specifications` entries keeps the filesystem layout configurable per repository and naturally supports multi-specification setups where each related specification contributes its own validation items.

## Acceptance Criteria

- When a `related_specifications` entry has a non-empty `local_path` that exists, all `.md` files with YAML frontmatter under that path are loaded as `ValidationItem` objects.
- When `local_path` is empty or the directory does not exist, that entry is skipped and no error is raised.
- When `related_specifications` is empty, no validation items are loaded and no error is raised.
