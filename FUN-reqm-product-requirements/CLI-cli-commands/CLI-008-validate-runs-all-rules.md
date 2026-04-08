---
id: CLI-008
title: validate command runs all defined validation rules
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [cli, validation]
relationships:
  derived_from: null
  related_to: [CLI-009, CLI-010, CLI-011]
---

## Description

The `reqm validate` command shall run all defined validation rules against the complete requirements collection.

## Rationale

Automated validation catches structural and referential errors early, before requirements are baselined or exported, reducing review effort and preventing broken exports.

## Acceptance Criteria

- `reqm validate` exercises every validation rule defined in `validate.py` against all discovered requirements.
