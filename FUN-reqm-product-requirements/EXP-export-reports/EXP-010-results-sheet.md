---
id: EXP-010
title: test-results exporter produces a Results sheet listing linked validation items
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [export, ecss, excel, testing]
relationships:
  derived_from: null
  related_to: [CLI-012, ARCH-001, EXP-011, EXP-012, EXP-013, EXP-014]
---

## Description

The `test-results` exporter shall produce an Excel workbook containing a sheet named "Results" with columns: Req ID, Item ID, Item Title.

## Rationale

Listing the validation plan — which items are linked to each requirement — enables auditors to verify coverage without duplicating execution results that are managed by external systems.

## Acceptance Criteria

- The output workbook contains a sheet named "Results".
- The sheet contains exactly the columns: Req ID, Item ID, Item Title — in that order.
- Each linked validation item occupies exactly one row.
- Requirements with no linked validation items produce no rows in the Results sheet.