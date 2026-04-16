---
id: REQM-ARCH-013
title: Tool discovers validation items from related_specifications with type validation_items
type: Functional
priority: High
status: Draft
stability: Evolving
verification: [Test]
tags: [architecture, metadata, validation]
relationships:
  derived_from: [REQM-ARCH-008]
  related_to: [REQM-EXP-017, REQM-ARCH-018]
---

## Description

The tool shall discover validation item files by reading the `type` field of each related specification before loading. For each entry in `related_specifications` whose `local_path` resolves to an existing directory, the tool shall load the specification metadata from that directory. Only entries whose specification declares `type: validation_items` are loaded as `ValidationItem` objects. Entries with an empty or absent `local_path`, or whose specification type is not `validation_items`, are skipped without error.

## Rationale

Tying validation item discovery to the `type` field of the related specification prevents requirements specifications from being mistakenly treated as validation item sources. This allows `related_specifications` to reference both requirements and validation items specifications without ambiguity.

## Acceptance Criteria

- For each entry in `related_specifications` whose `local_path` resolves to a directory containing a specification with `type: validation_items`, all `.md` files with YAML frontmatter under that path are loaded as `ValidationItem` objects.
- Entries whose related specification declares `type: requirements` (or any value other than `validation_items`) are silently skipped during item discovery.
- Entries with an empty `local_path` are silently skipped.
- Entries whose `local_path` does not exist are silently skipped.
- When `related_specifications` is empty, no validation items are loaded and no error is raised.
