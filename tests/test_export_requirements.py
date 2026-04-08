"""Tests for reqm.export.requirements — sheet names, columns, formatting."""
from pathlib import Path

from openpyxl import load_workbook

from reqm.export.requirements import RequirementsExporter
from reqm.fs import load_requirements, load_folder_meta


def test_requirements_exporter(fixtures_dir: Path, tmp_path: Path):
    reqs = load_requirements(fixtures_dir)
    folders = []
    meta = load_folder_meta(fixtures_dir)
    if meta:
        folders.append(meta)

    output = tmp_path / "requirements.xlsx"
    exporter = RequirementsExporter()
    exporter.export(reqs, folders, output)

    assert output.exists()

    wb = load_workbook(str(output))

    # Sheet names
    assert "Requirements" in wb.sheetnames
    assert "Folders" in wb.sheetnames

    # Requirements sheet headers
    ws_req = wb["Requirements"]
    headers = [cell.value for cell in ws_req[1]]
    assert headers == [
        "ID", "Title", "Description", "Rationale", "Acceptance Criteria",
        "Type", "Verification Method", "Derived From", "Related To", "Tags", "Folder ID",
    ]

    # Data rows exist
    assert ws_req.max_row > 1

    # Folders sheet
    ws_folders = wb["Folders"]
    folder_headers = [cell.value for cell in ws_folders[1]]
    assert folder_headers == ["ID", "Title", "Description"]

    # Tab colours are set
    assert ws_req.sheet_properties.tabColor is not None
    assert ws_folders.sheet_properties.tabColor is not None
    # Distinct colours
    assert ws_req.sheet_properties.tabColor != ws_folders.sheet_properties.tabColor

    # Freeze pane
    assert ws_req.freeze_panes == "A2"
    assert ws_folders.freeze_panes == "A2"

    # Header row is bold
    for cell in ws_req[1]:
        assert cell.font.bold is True
