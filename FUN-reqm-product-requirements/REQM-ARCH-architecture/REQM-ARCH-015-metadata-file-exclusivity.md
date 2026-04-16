---
id: REQM-ARCH-015
title: Tool errors when incompatible metadata files coexist in a directory
type: Constraint
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [architecture, metadata, validation]
relationships:
  derived_from: [REQM-ARCH-008, REQM-ARCH-014]
  related_to: [REQM-ARCH-017]
---

## Description

When `find_spec_root` encounters a directory containing any of the following incompatible pairs, the tool shall raise an error immediately and halt without loading any requirements:

- `.specification-metadata.md` and `.project-metadata.md` in the same directory
- `.specification-metadata.md` and `.folder-metadata.md` in the same directory

## Rationale

Each metadata file type has a distinct role: `.specification-metadata.md` marks a specification root, `.folder-metadata.md` marks a requirement subfolder, and `.project-metadata.md` is the legacy name for the specification root. Allowing incompatible pairs to coexist creates structural ambiguity and may cause the tool to silently ignore one file or produce incorrect results.

## Acceptance Criteria

- When both `.specification-metadata.md` and `.project-metadata.md` are present in the same directory, the tool exits with a non-zero status and an informative error message.
- When both `.specification-metadata.md` and `.folder-metadata.md` are present in the same directory, the tool exits with a non-zero status and an informative error message.
- No requirements are loaded or validated before the error is raised.
