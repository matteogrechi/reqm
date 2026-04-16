---
id: REQM-EXP-012
title: Item Count equals the number of validation items linked to each requirement
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [export, ecss, excel, testing]
relationships:
  derived_from: null
  related_to: [REQM-EXP-011]
---

## Description

For each requirement, the Item Count field in the Coverage sheet shall equal the number of entries in that requirement's `validated_by` list.

## Rationale

A count-based metric is the correct representation of the validation plan when execution results are managed externally; it avoids false precision from a pass/fail ratio that the tool cannot compute.

## Acceptance Criteria

- Item Count equals `len(validated_by)` for each requirement.
- Item Count is 0 for requirements with no `validated_by` entries.
- Item Count is a non-negative integer.