---
name: models
description: Guidelines and constraints for modifying reqm data models or requirement frontmatter schemas. Use when touching reqm/models.py, any requirement frontmatter, or the FolderMeta schema.
---

# Models Skill

Load this skill before touching `reqm/models.py` or any requirement frontmatter.

## Guardrails

- **Dataclasses only** — no I/O, no business logic, no methods beyond `__post_init__` for normalisation.
- **Add fields as optional with a default** — never break existing files.
- **New enum values must be added to both `models.py` and `validate.py`** — never add one without the other.
- **`extra: dict` absorbs unknown keys** — never raise on unknown frontmatter fields.
- **Do not add methods to dataclasses** — keep them as pure data containers.

## Workflow

### 1. Read the current model

Read `reqm/models.py` in full before making any changes.

### 2. Add the field

Add the new field as optional with a sensible default:

```python
new_field: str | None = None
```

### 3. Update validation

If the field has an allowed-values constraint, add the corresponding check in `reqm/validate.py`.
Use the validate skill if you are also touching validation logic.

### 4. Update the schema reference

Update the canonical schema block in `.claude/skills/incose-rewrite/SKILL.md` and
`.claude/skills/models/SKILL.md` to reflect the new field.

### 5. Run tests

```
pytest tests/
```

Fix until green.

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
  derived_from: [SYS-000]        #   one or more parent requirement IDs
  related_to: [SYS-002, SYS-003] # related requirement IDs
  validated_by: [TEST-001]       # linked test case IDs
---
```

## FolderMeta frontmatter — canonical schema (`.folder-metadata.md`)

```yaml
---
id: SYS                          # required — short folder identifier
title: "System Requirements"     # required
description: ""                  # optional — free text describing the folder's scope
---
```

## Folder naming convention

`KEY-slug` where `KEY` matches the folder's `id` field and `slug` is a short lowercase description.

Examples: `CLI-cli`, `ARCH-architecture`, `EXP-export`

## Done checklist

- [ ] New field added as optional with a default
- [ ] Enum values updated in both `models.py` and `validate.py` if applicable
- [ ] Schema blocks in both skill files updated
- [ ] `pytest tests/` passes
