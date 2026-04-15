---
id: EXP-015
title: Each sheet has a distinct tab colour
type: Constraint
priority: Low
status: Draft
stability: Stable
verification: [Inspection]
tags: [export, ecss, excel, formatting]
relationships:
  derived_from: null
  related_to: [EXP-003, EXP-005, EXP-009, EXP-014]
---

## Description

Each sheet within an exported workbook shall have a tab colour that differs from every other sheet's tab colour in that workbook.

## Rationale

Distinct tab colours allow reviewers to navigate quickly between sheets without reading the tab labels, reducing visual search time in multi-sheet workbooks.

## Acceptance Criteria

- Each sheet in a workbook has a tab colour set to a value that differs from all other sheets in the same workbook.
- The tab colour is visible in the Excel sheet tab bar.
