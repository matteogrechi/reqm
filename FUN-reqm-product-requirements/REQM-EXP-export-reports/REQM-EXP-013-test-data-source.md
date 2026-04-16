---
id: REQM-EXP-013
title: test-results exporter resolves validation items referenced by validated_by
type: Functional
priority: High
status: Draft
stability: Evolving
verification: [Test]
tags: [export, ecss, excel, testing]
relationships:
  derived_from: null
  related_to: [REQM-EXP-010, REQM-EXP-017]
---

## Description

The `test-results` exporter shall resolve each ID in a requirement's `validated_by` list against the collection of loaded `ValidationItem` objects and use the matched item's `title` in the Results sheet.

## Rationale

Keeping `validated_by` as a plain ID list — consistent with `derived_from` and `related_to` — and resolving titles at export time separates authoring from reporting and avoids data duplication.

## Acceptance Criteria

- For each ID in `validated_by`, the exporter resolves it to a `ValidationItem` and writes its `title` in the Item Title column.
- Requirements with no `validated_by` entries produce no rows in the Results sheet.
- IDs that do not resolve to a known `ValidationItem` produce a row with a blank Item Title.