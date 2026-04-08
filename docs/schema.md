# Requirement Schema

Each requirement is a Markdown file with YAML frontmatter.

## Frontmatter Fields

### Required

| Field | Type | Description |
|---|---|---|
| `id` | string | Unique identifier (e.g. `REQ-001`) |
| `title` | string | Human-readable title |
| `type` | string | One of: `Functional`, `Performance`, `Interface`, `Constraint` |
| `verification` | list | One or more of: `Test`, `Analysis`, `Inspection`, `Demonstration` |

### Optional

| Field | Type | Default | Description |
|---|---|---|---|
| `description` | section body | `""` | `## Description` section content |
| `rationale` | section body | `""` | `## Rationale` section content |
| `acceptance_criteria` | section body | `""` | `## Acceptance Criteria` section content |
| `tags` | list | `[]` | Free-form tags |
| `derived_from` | string | `null` | Parent requirement id (under `relationships`) |
| `related_to` | list | `[]` | Related requirement ids (under `relationships`) |
| `priority` | string | `null` | Priority level |
| `status` | string | `null` | Current status |
| `stability` | string | `null` | Stability indicator |
| `tests` | list | `[]` | Linked test case ids |

### Relationships Block

```yaml
relationships:
  derived_from: PARENT-ID
  related_to: [OTHER-ID-1, OTHER-ID-2]
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

## Example

```markdown
---
id: REQ-001
title: System shall authenticate users
type: Functional
verification: [Test, Analysis]
tags: [security]
relationships:
  derived_from: ARCH-001
  related_to: [REQ-002]
---

## Description

The system shall require valid credentials before granting access.

## Rationale

Security requirement mandated by compliance policy.

## Acceptance Criteria

- Login fails without credentials
- Login succeeds with valid credentials
```
