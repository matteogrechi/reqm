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
  related_to: [ARCH-002, ARCH-003]
---

## Description

The export subsystem shall use `AbstractExporter` defined in `reqm/export/base.py` as the sole plugin contract; every exporter shall subclass it and no other class.

## Rationale

A single abstract base class guarantees a uniform interface across all exporters, enables runtime discovery via entry points, and prevents format-specific logic from leaking into the CLI layer.

## Acceptance Criteria

- Every exporter class in the codebase subclasses `AbstractExporter` and no other class for the export contract.
- No exporter implements the export interface by any means other than subclassing `AbstractExporter`.
