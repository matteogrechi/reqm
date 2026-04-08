---
id: CLI-006
title: show command displays all frontmatter fields and body sections
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test]
tags: [cli, show]
relationships:
  derived_from: null
  related_to: [CLI-007]
---

## Description

The `reqm show <ID>` command shall display all frontmatter fields and all body sections (Description, Rationale, Acceptance Criteria) of the requirement identified by `<ID>`.

## Rationale

Authors frequently need to inspect a single requirement in complete detail — all metadata and body sections — without opening the raw file in an editor.

## Acceptance Criteria

- `reqm show CLI-001` outputs all frontmatter fields of the identified requirement.
- Each body section (Description, Rationale, Acceptance Criteria) is included in the output with its heading.
