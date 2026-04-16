# Exporters

reqm uses a plugin-based exporter system. Built-in exporters are registered via
`pyproject.toml` entry points under the `reqm.exporters` group.

## Usage

```sh
reqm export <exporter-name> -o output.xlsx
```

The exporter discovers the specification root automatically by walking upward
from the current directory until it finds `.specification-metadata.md`.

## Built-in Exporters

| Exporter | Output | Description |
|---|---|---|
| `requirements` | Single-sheet workbook | Folders and requirements interleaved |
| `traceability` | Two-sheet workbook | Parent→child matrix + orphans list |
| `test-results` | Two-sheet workbook | ECSS validation plan and coverage report |

### Requirements (`reqm export requirements`)

Produces a single-sheet workbook:

- **Requirements** sheet: `Is Folder | ID | Parent | Title | Description | Rationale | Acceptance Criteria | Type | Verification Method | Derived From | Related To | Tags | Path`

Folders and requirements are interleaved. Folder rows have `Is Folder=TRUE` and
carry `ID`, `Parent`, `Title`, `Description`, and `Path`; requirement-only
columns are left blank. Requirement rows have `Is Folder=FALSE` and `Parent`
set to the ID of the folder they belong to.

### Traceability (`reqm export traceability`)

Produces a workbook with:

- **Matrix** sheet: rows = parent requirements, columns = child requirements,
  `✓` at intersections where `child.derived_from == parent.id`
- **Orphans** sheet: requirements with no `derived_from` and no `related_to`

### Test Results (`reqm export test-results`)

Produces a workbook with:

- **Results** sheet: `Req ID | Item ID | Item Title` — one row per `validated_by`
  link, resolved against loaded `ValidationItem` objects.
- **Coverage** sheet: `Req ID | Title | Verified (Y/N) | Verification Method | Item Count`
  — one row per requirement; `Verified` is `Y` when at least one `validated_by`
  entry exists.

## Formatting

All exporters share a common style:

- Bold header row with `#BDD7EE` fill
- Freeze pane at `A2`
- Distinct tab colours per sheet

The Requirements exporter additionally sets an auto-filter on the sheet.

## Writing Custom Exporters

1. Subclass `AbstractExporter` in `reqm/export/` (or your own package).
2. Set `name` and `description` class attributes.
3. Implement `export(requirements, folders, items, output)`.
4. Register via entry point in `pyproject.toml`:

```toml
[project.entry-points."reqm.exporters"]
my-report = "my_package.my_module:MyExporter"
```

The CLI discovers and registers all entry points automatically.
