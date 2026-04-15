---
id: ARCH-001
title: AbstractExporter as sole plugin contract
type: Constraint
priority: High
status: Draft
stability: Stable
verification: [Inspection]
tags: [architecture, export, plugins]
relationships:
  derived_from: null
  related_to: [ARCH-002, ARCH-003, ARCH-012]
---

## Description

The `reqm` export framework shall designate `AbstractExporter` in `reqm/export/base.py` as the exclusive plugin contract for all exporters.

## Rationale

A single designated base class guarantees a uniform interface across all exporters, enables runtime discovery via entry points, and prevents format-specific logic from leaking into the CLI layer.

## Acceptance Criteria

- `reqm/export/base.py` defines a class named `AbstractExporter`.
- No other module in the codebase defines or exports an alternative plugin base class for exporters.
