---
id: EXP-005
title: All exporter sheets use explicit column widths and distinct tab colours
type: Functional
priority: Low
status: Draft
stability: Stable
verification: [Inspection]
tags: [export, ecss, excel, formatting]
relationships:
  derived_from: null
  related_to: [EXP-001, EXP-009, EXP-014]
---

## Description

All sheets produced by any exporter shall have explicitly set column widths, and each sheet within a workbook shall have a tab colour that is distinct from every other sheet's tab colour.

## Rationale

Explicit column widths ensure readability across different Excel versions and screen sizes. Distinct tab colours allow reviewers to navigate quickly between sheets without reading the tab labels.

## Acceptance Criteria

- No sheet uses the default (unset) column width; every column has an explicit width value.
- Each sheet within a workbook has a tab colour that differs from every other sheet's tab colour in that workbook.
