---
id: ARCH-011
title: Project metadata loads via fs.py function
type: Constraint
priority: High
status: Draft
stability: Volatile
verification: [Test, Inspection]
tags: [architecture, metadata, project]
relationships:
  derived_from: [ARCH-008]
  related_to: [ARCH-009, ARCH-010]
---

## Description

The `fs.py` module shall provide a `load_project_meta(root: Path) -> ProjectMeta` function that discovers and parses `.project-metadata.md`, returning a default `ProjectMeta` with empty values when the file is absent.

## Rationale

A dedicated loading function centralizes project metadata discovery and provides a consistent interface for all subsystems that need project-level context.

## Acceptance Criteria

- `load_project_meta` returns a `ProjectMeta` populated with `project_key` and `related_projects` when `.project-metadata.md` exists.
- `load_project_meta` returns a `ProjectMeta` with `project_key=""` and `related_projects=[]` when `.project-metadata.md` is absent.
- The `ProjectMeta` dataclass contains fields matching the frontmatter schema defined in ARCH-009 and ARCH-010.
