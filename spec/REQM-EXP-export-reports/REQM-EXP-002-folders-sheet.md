---
id: REQM-EXP-002
title: requirements exporter produces folder rows in the Requirements sheet
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [export, ecss, excel]
relationships:
  derived_from: null
  related_to: [REQM-EXP-001]
---

## Description

The `requirements` exporter shall include one row per discovered folder in the Requirements sheet. Each folder row shall populate the columns: Is Folder (TRUE), ID, Parent, Title, and Description. Columns specific to requirements (Rationale, Acceptance Criteria, Type, Verification Method, Derived From, Related To, Tags) shall be left blank for folder rows.

## Rationale

Interleaving folder rows with requirement rows in the same sheet provides reviewers with structural context about the requirements hierarchy. Including the folder description gives context about the purpose of each group without requiring reviewers to navigate the directory structure.

## Acceptance Criteria

- Each discovered folder occupies exactly one row in the Requirements sheet with Is Folder = TRUE.
- The folder row populates ID, Parent, Title, and Description; requirement-only columns are blank.
