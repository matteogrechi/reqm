---
id: EXP-014
title: test-results exporter applies standard sheet formatting
type: Functional
priority: Medium
status: Draft
stability: Stable
verification: [Inspection]
tags: [export, ecss, excel, testing, formatting]
relationships:
  derived_from: null
  related_to: [EXP-010, EXP-003, EXP-005]
---

## Description

All sheets produced by the `test-results` exporter shall apply the same header formatting, freeze pane, column widths, and tab colour conventions defined in EXP-003 and EXP-005.

## Rationale

Consistent formatting across all exporters gives the deliverable package a unified appearance and reduces reviewer context-switching between reports.

## Acceptance Criteria

- The Results and Coverage sheets conform to the header formatting specification in EXP-003 (bold, `#BDD7EE` fill, freeze pane).
- The Results and Coverage sheets conform to the column width and tab colour specification in EXP-005.
