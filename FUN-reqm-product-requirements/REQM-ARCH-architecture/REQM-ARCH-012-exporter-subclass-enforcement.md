---
id: REQM-ARCH-012
title: Every exporter subclasses AbstractExporter exclusively
type: Constraint
priority: High
status: Draft
stability: Stable
verification: [Inspection]
tags: [architecture, export, plugins]
relationships:
  derived_from: [REQM-ARCH-001]
  related_to: [REQM-ARCH-002]
---

## Description

Every exporter class shall subclass `AbstractExporter` and no other class to implement the plugin interface.

## Rationale

Enforcing that all exporters subclass only `AbstractExporter` ensures the runtime discovery mechanism works uniformly and prevents exporters from depending on private implementation details of unrelated classes.

## Acceptance Criteria

- Every concrete exporter class in the codebase subclasses `AbstractExporter`.
- No concrete exporter class subclasses any class other than `AbstractExporter` for the purpose of implementing the plugin interface.