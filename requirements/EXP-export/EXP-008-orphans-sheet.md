---
id: EXP-008
title: traceability exporter produces an Orphans sheet
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [export, ecss, excel, traceability]
relationships:
  derived_from: null
  related_to: [EXP-006]
---

## Description

The `traceability` exporter shall produce an Excel workbook containing a sheet named "Orphans" that lists all requirements having neither a `derived_from` link nor any `related_to` link, with columns: ID, Title, Folder ID.

## Rationale

Orphaned requirements are a gap indicator in the traceability chain. Isolating them in a dedicated sheet draws reviewer attention to potential omissions without cluttering the main matrix.

## Acceptance Criteria

- The output workbook contains a sheet named "Orphans".
- Every requirement with no `derived_from` and no `related_to` appears in the Orphans sheet.
- Requirements with at least one `derived_from` or `related_to` link are absent from the Orphans sheet.
- The sheet contains exactly the columns: ID, Title, Folder ID.
