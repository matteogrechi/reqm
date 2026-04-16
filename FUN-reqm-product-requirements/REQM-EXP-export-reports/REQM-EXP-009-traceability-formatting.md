---
id: REQM-EXP-009
title: traceability exporter applies standard sheet formatting
type: Functional
priority: Medium
status: Draft
stability: Stable
verification: [Inspection]
tags: [export, ecss, excel, traceability, formatting]
relationships:
  derived_from: null
  related_to: [REQM-EXP-006, REQM-EXP-003, REQM-EXP-005, REQM-EXP-015]
---

## Description

All sheets produced by the `traceability` exporter shall apply the header formatting, freeze pane, column widths, and tab colour conventions defined in REQM-EXP-003, REQM-EXP-005, and REQM-EXP-015.

## Rationale

Consistent formatting across all exporters gives the deliverable package a unified appearance and reduces reviewer context-switching between reports.

## Acceptance Criteria

- The Matrix and Orphans sheets conform to the header formatting specification in REQM-EXP-003 (bold, `#BDD7EE` fill, freeze pane).
- The Matrix and Orphans sheets conform to the column width specification in REQM-EXP-005.
- The Matrix and Orphans sheets conform to the tab colour specification in REQM-EXP-015.
