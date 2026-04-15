---
id: EXP-011
title: test-results exporter produces a Coverage sheet with per-requirement item counts
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [export, ecss, excel, testing]
relationships:
  derived_from: null
  related_to: [EXP-010, EXP-012]
---

## Description

The `test-results` exporter shall produce an Excel workbook containing a sheet named "Coverage" with columns: Req ID, Title, Verified (Y/N), Verification Method, Item Count.

## Rationale

A coverage summary gives reviewers a single-page view of which requirements have at least one validation item linked, without requiring them to scan individual validation item records.

## Acceptance Criteria

- The output workbook contains a sheet named "Coverage".
- The sheet contains exactly the columns: Req ID, Title, Verified (Y/N), Verification Method, Item Count — in that order.
- Each requirement occupies exactly one row.
- Verified is "Y" when the requirement has at least one linked validation item; "N" otherwise.