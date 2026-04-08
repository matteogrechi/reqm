---
id: EXP-003
title: All exporter sheets use standard header formatting
type: Functional
priority: Medium
status: Draft
stability: Stable
verification: [Inspection]
tags: [export, ecss, excel, formatting]
relationships:
  derived_from: null
  related_to: [EXP-001, EXP-009, EXP-014]
---

## Description

All sheets produced by any exporter shall have a header row that is bold, filled with colour `#BDD7EE`, and has a freeze pane applied immediately below it.

## Rationale

Consistent header formatting improves readability and aligns with ECSS document conventions used in project reviews and audits.

## Acceptance Criteria

- On every sheet in every exported workbook, the header row font is bold.
- On every sheet, the header row fill colour is `#BDD7EE`.
- On every sheet, the pane is frozen below row 1 (the header row).
