---
id: REQM-ARCH-011
title: Specification metadata loads via fs.py functions
type: Constraint
priority: High
status: Draft
stability: Volatile
verification: [Test, Inspection]
tags: [architecture, metadata, specification]
relationships:
  derived_from: [REQM-ARCH-008]
  related_to: [REQM-ARCH-009, REQM-ARCH-010, REQM-ARCH-014]
---

## Description

The `fs.py` module shall provide two functions for working with specification metadata: `find_spec_root(start: Path) -> Path`, which navigates upward from `start` to locate the directory containing `.specification-metadata.md`, and `load_spec_meta(root: Path) -> SpecMeta`, which parses the file and returns a populated `SpecMeta` instance. When `.specification-metadata.md` is absent, `load_spec_meta` returns a default `SpecMeta` with empty values.

## Rationale

Separating root discovery from metadata parsing keeps each function single-purpose and allows callers that already know the root (e.g. tests) to call `load_spec_meta` directly without triggering a filesystem walk.

## Acceptance Criteria

- `find_spec_root` returns the first ancestor directory (inclusive of `start`) that contains `.specification-metadata.md`.
- `find_spec_root` raises `FileNotFoundError` when no such directory is found before the filesystem root.
- `load_spec_meta` returns a `SpecMeta` populated with `id`, `title`, and `related_specifications` when `.specification-metadata.md` exists.
- `load_spec_meta` returns a `SpecMeta` with `id=""`, `title=""`, and `related_specifications=[]` when `.specification-metadata.md` is absent.
- The `SpecMeta` dataclass contains fields matching the frontmatter schema defined in REQM-ARCH-009 and REQM-ARCH-010.
