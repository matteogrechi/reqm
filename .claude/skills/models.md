# Skill: Models and Frontmatter Schema

Load this file before touching `reqm/models.py` or any requirement frontmatter.

## Requirement frontmatter — canonical schema

```yaml
---
id: SYS-001                      # required — unique across the repo
title: "Short imperative title"  # required
type: Functional                 # required — Functional | Performance | Interface | Constraint
priority: High                   # required — Critical | High | Medium | Low
status: Draft                    # required — Draft | Approved | Deprecated
stability: Stable                # required — Volatile | Stable | Locked
verification: [Test]             # required — one or more of: Test | Analysis | Inspection | Demonstration
tags: [power, startup]           # optional
relationships:                   # optional block
  derived_from: null             #   ID of parent requirement
  related_to: [SYS-002, SYS-003] # related requirement IDs
---
```

### INCOSE fields

`priority`, `status`, and `stability` were added for INCOSE compliance.
They are optional in the dataclass (defaults: `priority=None`, `status=None`, `stability=None`)
until the model is updated, but **all new and rewritten requirements must include them**.
See `.claude/skills/incose-rewrite.md` for allowed values and semantics.

The markdown body below the frontmatter must contain exactly three sections:

```markdown
## Description
<what the system shall do>

## Rationale
<why this requirement exists>

## Acceptance Criteria
<conditions that must be met for the requirement to be considered satisfied>
```

All three sections are required in the file; each maps to a named field on `Requirement`
(`description`, `rationale`, `acceptance_criteria`).

## Folder naming convention

Requirement folders must be named `KEY-slug`, where `KEY` matches the folder's
`id` field and `slug` is a short lowercase description, e.g. `CLI-cli`,
`ARCH-architecture`, `EXP-export`.

## FolderMeta frontmatter — canonical schema (`.folder-metadata.md`)

```yaml
---
id: SYS                        # required — short folder identifier
title: "System Requirements"   # required
---
```

The markdown body below the frontmatter contains one optional section:

```markdown
## Description
<free text describing the folder's scope and contents>
```

## Rules for evolving models

- Add fields as optional with a default — never break existing files
- New enumeration values must be added to both the model and `validate.py`
- `extra: dict` absorbs unknown keys gracefully — never raise on unknown fields
- Do not add methods to dataclasses — keep them as pure data containers
