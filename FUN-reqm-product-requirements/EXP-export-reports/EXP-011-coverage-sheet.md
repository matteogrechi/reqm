---
id: EXP-011
title: test-results exporter produces a Coverage sheet
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

The `test-results` exporter shall produce an Excel workbook containing a sheet named "Coverage" with columns: Req ID, Title, Verified (Yes/No), Verification Method, Coverage %.

## Rationale

A coverage summary gives reviewers a single-page view of verification completeness across all requirements, without requiring them to scan individual test records.

## Acceptance Criteria

- The output workbook contains a sheet named "Coverage".
- The sheet contains exactly the columns: Req ID, Title, Verified, Verification Method, Coverage % — in that order.
- Each requirement occupies exactly one row.
