---
id: REQM-EXP-006
title: traceability exporter produces a Matrix sheet with derived_from links
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [export, ecss, excel, traceability]
relationships:
  derived_from: null
  related_to: [REQM-CLI-012, REQM-ARCH-001, REQM-EXP-007, REQM-EXP-008, REQM-EXP-009]
---

## Description

The `traceability` exporter shall produce an Excel workbook containing a sheet named "Matrix" where rows represent parent requirements, columns represent the IDs of requirements that derive from them, and a `✓` mark appears at each valid intersection.

## Rationale

A traceability matrix is a mandatory ECSS deliverable that demonstrates every derived requirement is linked to a higher-level parent requirement.

## Acceptance Criteria

- The output workbook contains a sheet named "Matrix".
- A `✓` appears at intersection `(R, C)` for every requirement `C` that has `derived_from: R`.
- All other intersections in the matrix are empty.
