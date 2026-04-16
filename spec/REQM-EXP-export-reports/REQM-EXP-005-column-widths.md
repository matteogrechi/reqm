---
id: REQM-EXP-005
title: All exporter sheets use explicit column widths
type: Constraint
priority: Low
status: Draft
stability: Stable
verification: [Inspection]
tags: [export, ecss, excel, formatting]
relationships:
  derived_from: null
  related_to: [REQM-EXP-001, REQM-EXP-003, REQM-EXP-006, REQM-EXP-009, REQM-EXP-010, REQM-EXP-014, REQM-EXP-015]
---

## Description

All sheets produced by any exporter shall set an explicit width value for every column.

## Rationale

Explicit column widths ensure readability across different Excel versions and screen sizes, preventing columns from collapsing to unusable default widths.

## Acceptance Criteria

- No sheet uses the default (unset) column width; every column has an explicit width value set.
- Column widths are set to values that display typical cell content without truncation.
