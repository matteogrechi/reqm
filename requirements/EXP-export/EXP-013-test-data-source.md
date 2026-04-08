---
id: EXP-013
title: test-results exporter reads test data from the frontmatter tests key
type: Functional
priority: High
status: Draft
stability: Volatile
verification: [Test]
tags: [export, ecss, excel, testing]
relationships:
  derived_from: null
  related_to: [EXP-010]
---

## Description

The `test-results` exporter shall read test outcome data exclusively from files referenced in requirement frontmatter under the `tests` key.

## Rationale

Storing test references in requirement frontmatter keeps the linkage co-located with the requirement definition and uses the same git-native storage model as the requirements themselves.

## Acceptance Criteria

- Test outcome records are derived only from files referenced by the `tests` frontmatter key.
- Requirements with no `tests` frontmatter key produce no rows in the Results sheet.

**Note**: The structure and file format of the referenced test result files is specified by a separate, pending requirement. Until that requirement is approved, this requirement retains `stability: Volatile`.
