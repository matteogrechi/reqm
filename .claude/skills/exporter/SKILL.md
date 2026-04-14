---
name: exporter
description: Guidelines and constraints for writing or modifying reqm exporters. Use when touching any file in reqm/export/ or adding a new exporter to the project.
---

# Exporter Skill

Load this skill before touching anything in `reqm/export/`.

## Guardrails

- **Every exporter must subclass `AbstractExporter`** from `reqm/export/base.py` — never subclass anything else.
- **CLI discovery is entry-point only** — never add exporter names or imports to `cli.py`.
- **Excel exporters use `openpyxl` only** — no other Excel library.
- **One exporter per file** — no cross-dependencies between exporter modules.
- **Do not add methods to `AbstractExporter`** unless a requirement explicitly calls for it.

## Workflow

### 1. Read the contract

Read `reqm/export/base.py` to confirm the current `AbstractExporter` interface before writing a single line.

### 2. Create the exporter module

Create `reqm/export/<name>.py`. Implement:

- `name: str` — CLI subcommand name (class attribute)
- `description: str` — one-line description (class attribute)
- `export(requirements, folders, output)` — the only required method

### 3. Register the entry point

Add to `pyproject.toml` under `[project.entry-points."reqm.exporters"]`:

```toml
<name> = "reqm.export.<name>:<ClassName>"
```

### 4. Test

Write `tests/test_export_<name>.py`. Cover at minimum:
- Happy path with valid requirements
- Empty requirements list
- Output file is created and is valid

Run: `pytest tests/test_export_<name>.py`

### 5. Document

Add the exporter to `docs/exporters.md`.

## Excel conventions (ECSS)

| Setting | Value |
|---|---|
| Header fill | Bold, light blue `#BDD7EE` |
| Freeze pane | Row immediately below the header |
| Auto-filter | On every sheet |
| Column widths | Set explicitly — never rely on defaults |
| Tab colour | Must be set on every sheet |
| Merged cells | Cover/summary areas only — not data rows |

## Done checklist

- [ ] Subclasses `AbstractExporter` and nothing else
- [ ] `name` and `description` set as class attributes
- [ ] `export()` implemented with a Google-style docstring
- [ ] Entry point registered in `pyproject.toml`
- [ ] `pytest tests/test_export_<name>.py` passes
- [ ] Documented in `docs/exporters.md`
