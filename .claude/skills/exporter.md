# Skill: Writing an Exporter

Load this file before touching anything in `reqm/export/`.

## Contract

Every exporter must:
1. Subclass `AbstractExporter` from `reqm/export/base.py`
2. Set `name` (the CLI subcommand) and `description` (one line)
3. Implement `export(requirements, folders, output)` — the only required method
4. Be registered in `pyproject.toml` under `[project.entry-points."reqm.exporters"]`
5. Be discoverable by the CLI without any changes to `cli.py`

## Excel conventions (ECSS)

- Use `openpyxl` — no other Excel library
- Header row: bold, light blue fill (`BDD7EE`), freeze pane below it
- Auto-filter on every sheet
- Column widths: set explicitly, never rely on defaults
- No merged cells except in cover/summary areas
- All sheets must have a tab colour set

## Adding a new exporter checklist

- [ ] New file in `reqm/export/<name>.py`
- [ ] Class subclasses `AbstractExporter`
- [ ] `name` and `description` set as class attributes
- [ ] `export()` implemented and documented
- [ ] Entry point added to `pyproject.toml`
- [ ] At least one test in `tests/test_export_<name>.py`
- [ ] Documented in `docs/exporters.md`
