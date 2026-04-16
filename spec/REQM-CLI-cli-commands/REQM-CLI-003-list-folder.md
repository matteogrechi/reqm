---
id: REQM-CLI-003
title: list --folder option filters output by folder ID
type: Functional
priority: Medium
status: Draft
stability: Stable
verification: [Test]
tags: [cli, list]
relationships:
  derived_from: null
  related_to: [REQM-CLI-001]
---

## Description

The `reqm list` command shall accept a `--folder <ID>` option that restricts output to requirements belonging to the folder with the given ID.

## Rationale

Large requirements sets span multiple folders; a folder filter lets authors review a single workstream without noise from unrelated folders.

## Acceptance Criteria

- `reqm list --folder REQM-CLI` returns only requirements whose Folder ID is `REQM-CLI`.
- Requirements in folders other than the specified one are absent from the output.
