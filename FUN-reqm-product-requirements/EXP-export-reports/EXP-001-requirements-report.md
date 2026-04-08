---
id: EXP-001
title: requirements exporter produces a Requirements sheet
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [export, ecss, excel]
relationships:
  derived_from: null
  related_to: [CLI-012, ARCH-001, EXP-002, EXP-003, EXP-004, EXP-005]
---

## Description

The `requirements` exporter shall produce an Excel workbook containing a sheet named "Requirements" with columns: ID, Title, Description, Rationale, Acceptance Criteria, Type, Verification Method, Derived From, Related To, Tags, Folder ID.

## Rationale

An ECSS-compliant flat requirements list is the standard deliverable for project reviews and audits. Separate columns for each body section allow reviewers to assess completeness at a glance without opening individual files.

## Acceptance Criteria

- The output workbook contains a sheet named "Requirements".
- The sheet contains exactly the columns: ID, Title, Description, Rationale, Acceptance Criteria, Type, Verification Method, Derived From, Related To, Tags, Folder ID — in that order.
- Each discovered requirement occupies exactly one row.
