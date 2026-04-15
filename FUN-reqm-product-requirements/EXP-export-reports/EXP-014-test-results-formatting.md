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
  related_to: [EXP-010, EXP-003, EXP-005, EXP-015]
---

## Description

All sheets produced by the `test-results` exporter shall apply the header formatting, freeze pane, column widths, and tab colour conventions defined in EXP-003, EXP-005, and EXP-015.

## Rationale

Consistent formatting across all exporters gives the deliverable package a unified appearance and reduces reviewer context-switching between reports.

## Acceptance Criteria

- The Results and Coverage sheets conform to the header formatting specification in EXP-003 (bold, `#BDD7EE` fill, freeze pane).
- The Results and Coverage sheets conform to the column width specification in EXP-005.
- The Results and Coverage sheets conform to the tab colour specification in EXP-015.
