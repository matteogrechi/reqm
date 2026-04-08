---
id: EXP-012
title: Coverage % is computed as passed tests divided by total linked tests
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [export, ecss, excel, testing]
relationships:
  derived_from: null
  related_to: [EXP-011]
---

## Description

The Coverage % value for each requirement shall be computed as the ratio of passed tests to the total number of tests linked to that requirement, expressed as a percentage rounded to two decimal places.

## Rationale

A ratio-based coverage metric is the standard ECSS measure of verification completeness; it accounts for partial coverage and distinguishes passed tests from merely executed ones.

## Acceptance Criteria

- Coverage % = (count of linked tests with Result = "Pass") / (count of all linked tests) × 100, rounded to two decimal places.
- A requirement with no linked tests displays a Coverage % of 0.00.
