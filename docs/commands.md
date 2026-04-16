# CLI Commands

## `reqm list`

List all requirements in the current specification.

```sh
reqm list
reqm list --folder REQM-FUN
reqm list --status Draft
```

Options:

| Option | Description |
|---|---|
| `--folder` | Filter by folder ID (e.g. `REQM-FUN`) |
| `--status` | Filter by status value (e.g. `Draft`, `Approved`, `Deprecated`) |

Output columns: `ID | Title | Type | Verification | Folder ID`

## `reqm show <req_id>`

Display all fields of a single requirement.

```sh
reqm show REQM-FUN-001
```

Prints every populated field — description, rationale, and acceptance criteria
are shown as labelled blocks when present.

Exits non-zero with an error message if the ID is not found.

## `reqm validate`

Validate all requirements in the specification. See [validation.md](validation.md)
for the full rule reference.

```sh
reqm validate
```

## `reqm export <name>`

Export requirements to an Excel report. See [exporters.md](exporters.md) for
available exporters and their output formats.

```sh
reqm export requirements -o report.xlsx
reqm export traceability -o matrix.xlsx
reqm export test-results -o coverage.xlsx
```
