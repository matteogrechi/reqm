---
id: EXP-002
title: requirements exporter produces a Folders sheet
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [export, ecss, excel]
relationships:
  derived_from: null
  related_to: [EXP-001]
---

## Description

The `requirements` exporter shall produce an Excel workbook containing a sheet named "Folders" with columns: ID, Title, Description.

## Rationale

A Folders sheet provides reviewers with context about the requirements hierarchy without requiring them to navigate the directory structure directly.

## Acceptance Criteria

- The output workbook contains a sheet named "Folders".
- The sheet contains exactly the columns: ID, Title, Description — in that order.
- Each discovered folder occupies exactly one row.
