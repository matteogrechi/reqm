---
id: EXP-010
title: test-results exporter produces a Results sheet
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

The `test-results` exporter shall produce an Excel workbook containing a sheet named "Results" with columns: Req ID, Test ID, Test Title, Result (Pass/Fail/Blocked/Not Run), Date, Notes.

## Rationale

Linking test outcomes to requirements in a structured sheet enables auditors to verify that each requirement has been covered by at least one test, as required by ECSS.

## Acceptance Criteria

- The output workbook contains a sheet named "Results".
- The sheet contains exactly the columns: Req ID, Test ID, Test Title, Result, Date, Notes — in that order.
- Each test outcome record occupies exactly one row.
