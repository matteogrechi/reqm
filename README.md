# reqm

Minimal requirements manager. Read, validate, export — nothing else.

## Install

### Requirements

- **Python** ≥ 3.14
- **pip** (or **uv** for faster installs)
- Supported platforms: macOS, Linux

### From source (development)

```bash
# Recommended — install + dev dependencies via uv
make install-dev

# Or manually
uv sync --all-extras
```

### As a package

```bash
pip install .
# or
uv pip install .
```

Dependencies installed automatically:

- **click** — CLI framework
- **pyyaml** — YAML frontmatter parsing
- **openpyxl** — Excel export
- **pytest** (dev extra) — test suite

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
spec/
├── .specification-metadata.md     # spec root marker (id, related_specifications)
├── REQM-ARCH-architecture/
│   ├── .folder-metadata.md        # folder id + title
│   ├── REQM-ARCH-001-*.md         # one file per requirement
│   └── ...
├── REQM-CLI-cli-commands/
│   ├── .folder-metadata.md
│   └── ...
└── REQM-EXP-export-reports/
    ├── .folder-metadata.md
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
3. Implement `export(requirements, folders, items, output)`
4. Register in `pyproject.toml`:

   ```toml
   [project.entry-points."reqm.exporters"]
   my-report = "my_package:MyExporter"
   ```

See `.claude/skills/exporter.md` for full conventions.
