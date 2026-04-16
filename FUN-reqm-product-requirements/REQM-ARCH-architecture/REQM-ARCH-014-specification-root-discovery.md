---
id: REQM-ARCH-014
title: Tool discovers specification root by walking up the file system
type: Functional
priority: High
status: Draft
stability: Volatile
verification: [Test]
tags: [architecture, discovery, specification]
relationships:
  derived_from: null
  related_to: [REQM-ARCH-008, REQM-ARCH-011, REQM-ARCH-015]
---

## Description

The tool shall determine the specification root by walking upward from the current working directory, stopping at the first directory that contains a `.specification-metadata.md` file. The directory containing that file is the specification root used for all subsequent operations.

## Rationale

Auto-discovery eliminates the need for an explicit `--root` flag and allows the tool to be invoked from any subdirectory of the specification, matching the ergonomics of tools like git.

## Acceptance Criteria

- When invoked from any subdirectory of a specification, the tool identifies the correct specification root.
- When no `.specification-metadata.md` file is found in any ancestor directory, the tool exits with a clear error message.
- The discovered root is used for requirement discovery, validation, and export without requiring additional user input.
