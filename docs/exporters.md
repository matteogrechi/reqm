# Exporters

reqm uses a plugin-based exporter system. Built-in exporters are registered via
`pyproject.toml` entry points under the `reqm.exporters` group.

## Usage

```sh
reqm export <exporter-name> -o output.xlsx
reqm export <exporter-name> --root custom/requirements -o output.xlsx
```

## Built-in Exporters

| Exporter | Output | Description |
|---|---|---|
| `requirements` | Two-sheet workbook | Requirements list + folder summary |
| `traceability` | Two-sheet workbook | Parent→child matrix + orphans list |
| `test-results` | Two-sheet workbook | Test results + coverage report |

### Requirements (`reqm export requirements`)

Produces a workbook with:

- **Requirements** sheet: `ID | Title | Description | Rationale | Acceptance Criteria | Type | Verification Method | Derived From | Related To | Tags | Folder ID`
- **Folders** sheet: `ID | Title | Description`

### Traceability (`reqm export traceability`)

Produces a workbook with:

- **Matrix** sheet: rows = parent requirements, columns = child requirements,
  `✓` at intersections where `child.derived_from == parent.id`
- **Orphans** sheet: requirements with no `derived_from` and no `related_to`

### Test Results (`reqm export test-results`)

Produces a workbook with:

- **Results** sheet: `Req ID | Test ID | Test Title | Result | Date | Notes`
- **Coverage** sheet: `Req ID | Title | Verified (Y/N) | Method | Coverage %`

> **Note**: Test outcome data loading is stubbed pending EXP-013 (test file format
> not yet specified).

## Formatting

All exporters share a common style:

- Bold header row with `#BDD7EE` fill
- Freeze pane at `A2`
- Distinct tab colours per sheet
- Auto-filter on the Requirements sheet

## Writing Custom Exporters

1. Subclass `AbstractExporter` in `reqm/export/` (or your own package).
2. Set `name` and `description` class attributes.
3. Implement `export(requirements, folders, output)`.
4. Register via entry point in `pyproject.toml`:

```toml
[project.entry-points."reqm.exporters"]
my-report = "my_package.my_module:MyExporter"
```

The CLI discovers and registers all entry points automatically.
