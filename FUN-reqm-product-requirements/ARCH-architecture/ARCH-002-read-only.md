---
id: ARCH-002
title: Entry-point-based exporter registration
type: Constraint
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [architecture, export, plugins]
relationships:
  derived_from: null
  related_to: [ARCH-001, ARCH-003]
---

## Description

New exporters shall be registerable by adding an entry point to `pyproject.toml` under the `reqm.exporters` group, without modifying any core source file.

## Rationale

Entry-point registration allows third-party exporters to extend reqm without forking or patching the core codebase, keeping the tool open for extension and closed for modification.

## Acceptance Criteria

- A new exporter registered solely via a `pyproject.toml` entry point is invocable through `reqm export`.
- Removing the entry point from `pyproject.toml` removes the exporter from the CLI without any code changes.
