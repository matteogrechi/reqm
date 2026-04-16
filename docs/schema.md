# Requirement Schema

Each requirement is a Markdown file with YAML frontmatter.

## Frontmatter Fields

### Required

| Field | Type | Description |
|---|---|---|
| `id` | string | Unique identifier following the format `<specification_key>-<folder_key>-NNN` (e.g. `REQM-FUN-001`) |
| `title` | string | Human-readable title |
| `type` | string | One of: `Functional`, `Performance`, `Interface`, `Constraint` |
| `verification` | list | One or more of: `Test`, `Analysis`, `Inspection`, `Demonstration` |

### Optional

| Field | Type | Default | Description |
|---|---|---|---|
| `priority` | string | `null` | One of: `Critical`, `High`, `Medium`, `Low` |
| `status` | string | `null` | One of: `Draft`, `Approved`, `Deprecated` |
| `stability` | string | `null` | One of: `Volatile`, `Stable`, `Locked` |
| `tags` | list | `[]` | Free-form tags |
| `relationships` | block | — | See Relationships Block below |

### Relationships Block

All inter-requirement links live under the `relationships` key:

```yaml
relationships:
  derived_from: [PARENT-ID]         # list — one or more parent requirement IDs
  related_to: [OTHER-ID-1, OTHER-ID-2]  # list — horizontally related requirements
  validated_by: [TEST-001]          # list — linked test case IDs
```

### Unknown Keys

Any frontmatter key not in the known set is stored in the `extra` dict.

## Body Sections

Three section headings are recognized in the markdown body (after the closing `---`):

- `## Description` → `description` field
- `## Rationale` → `rationale` field
- `## Acceptance Criteria` → `acceptance_criteria` field

## Folder Metadata

Each folder may contain a `.folder-metadata.md` file with frontmatter:

```yaml
---
id: FOLDER-ID
title: Folder Title
description: Optional description
---
```

## Specification Metadata

The specification root may contain a `.specification-metadata.md` file. The tool
discovers the root by walking upward from the current directory until it finds this
file. Only one of `.specification-metadata.md` or `.project-metadata.md` may exist
in any directory.

```yaml
---
specification_key: REQM
related_specifications:
  - id: SYS
    local_path: ../sys-arch
---
```

| Field                    | Description                                                                                    |
|--------------------------|------------------------------------------------------------------------------------------------|
| `specification_key`      | Short identifier for this specification; used as the first segment of all requirement IDs.     |
| `related_specifications` | Related specifications; each entry has `id` and `local_path`.                                  |

## Example

```markdown
---
id: REQM-FUN-001
title: System shall authenticate users
type: Functional
priority: High
status: Draft
stability: Stable
verification: [Test, Analysis]
tags: [security]
relationships:
  derived_from: [REQM-ARCH-001]
  related_to: [REQM-FUN-002]
  validated_by: [TEST-001]
---

## Description

The system shall require valid credentials before granting access.

## Rationale

Security requirement mandated by compliance policy.

## Acceptance Criteria

- Login fails without credentials
- Login succeeds with valid credentials
```
