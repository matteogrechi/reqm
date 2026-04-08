# reqm

Minimal requirements manager. Read, validate, export — nothing else.

## Install

### Requirements

- **Python** ≥ 3.14
- **pip** (or **uv** for faster installs)
- Supported platforms: macOS, Linux

### Steps

```bash
# Using pip
pip install -e ".[dev]"

# Using uv (recommended)
uv sync --all-extras
```

This installs `reqm` in editable mode along with its dependencies:
- **click** — CLI framework
- **pyyaml** — YAML frontmatter parsing
- **openpyxl** — Excel export
- **pytest** (dev) — test suite

## Usage

```bash
reqm list                          # list all requirements
reqm list --folder CLI             # filter by folder
reqm list --status Draft           # filter by status
reqm show SYS-001                  # display a requirement
reqm validate                      # validate all requirements
reqm export requirements -o r.xlsx # export requirements list
reqm export traceability -o t.xlsx # export traceability matrix
reqm export test-results -o v.xlsx # export test results
```

## Requirements are markdown files

```text
FUN-reqm-product-requirements/
├── .folder-metadata.md            # folder metadata
├── CLI-cli-commands/
│   ├── .folder-metadata.md
│   └── CLI-001-list.md            # one file per requirement
└── EXP-export-reports/
    └── ...
```

Each file has YAML frontmatter followed by three structured body sections:

```markdown
---
id: CLI-001
title: List requirements
type: Functional
verification: Test
tags: [cli]
---

## Description
The tool shall ...

## Rationale
...

## Acceptance Criteria
- ...
```

## Adding a custom exporter

1. Subclass `reqm.export.base.AbstractExporter`
2. Set `name` and `description`
3. Implement `export(requirements, folders, output)`
4. Register in `pyproject.toml`:

   ```toml
   [project.entry-points."reqm.exporters"]
   my-report = "my_package:MyExporter"
   ```

See `.claude/skills/exporter.md` for full conventions.
