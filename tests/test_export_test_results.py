"""Tests for reqm.export.test_results — sheet names, coverage calc."""
from pathlib import Path

from openpyxl import load_workbook

from reqm.export.test_results import TestResultsExporter
from reqm.fs import load_requirements, load_folder_meta


def test_test_results_exporter(fixtures_dir: Path, tmp_path: Path):
    reqs = load_requirements(fixtures_dir)
    folders = []
    meta = load_folder_meta(fixtures_dir)
    if meta:
        folders.append(meta)

    output = tmp_path / "test_results.xlsx"
    exporter = TestResultsExporter()
    exporter.export(reqs, folders, output)

    assert output.exists()

    wb = load_workbook(str(output))
    assert "Results" in wb.sheetnames
    assert "Coverage" in wb.sheetnames


def test_results_sheet_headers(fixtures_dir: Path, tmp_path: Path):
    reqs = load_requirements(fixtures_dir)
    folders = []
    meta = load_folder_meta(fixtures_dir)
    if meta:
        folders.append(meta)

    output = tmp_path / "results_hdr.xlsx"
    exporter = TestResultsExporter()
    exporter.export(reqs, folders, output)

    wb = load_workbook(str(output))
    ws = wb["Results"]
    headers = [cell.value for cell in ws[1]]
    assert headers == ["Req ID", "Test ID", "Test Title", "Result", "Date", "Notes"]


def test_coverage_sheet_headers(fixtures_dir: Path, tmp_path: Path):
    reqs = load_requirements(fixtures_dir)
    folders = []
    meta = load_folder_meta(fixtures_dir)
    if meta:
        folders.append(meta)

    output = tmp_path / "coverage_hdr.xlsx"
    exporter = TestResultsExporter()
    exporter.export(reqs, folders, output)

    wb = load_workbook(str(output))
    ws = wb["Coverage"]
    headers = [cell.value for cell in ws[1]]
    assert headers == ["Req ID", "Title", "Verified (Y/N)", "Method", "Coverage %"]


def test_coverage_calc_zero_tests(fixtures_dir: Path, tmp_path: Path):
    """Requirements with no tests should show 0 coverage."""
    reqs = load_requirements(fixtures_dir)
    folders = []
    meta = load_folder_meta(fixtures_dir)
    if meta:
        folders.append(meta)

    output = tmp_path / "coverage_zero.xlsx"
    exporter = TestResultsExporter()
    exporter.export(reqs, folders, output)

    wb = load_workbook(str(output))
    ws = wb["Coverage"]

    # Build a map: req_id → coverage%
    coverage_map = {}
    for row in ws.iter_rows(min_row=2, values_only=False):
        req_id = row[0].value
        cov_pct = row[4].value
        coverage_map[req_id] = cov_pct

    # A has no tests → 0
    assert coverage_map.get("A") == 0
    # D has no tests → 0
    assert coverage_map.get("D") == 0


def test_coverage_calc_with_tests(fixtures_dir: Path, tmp_path: Path):
    """Requirements with tests should show coverage (stubbed to 0% for now)."""
    reqs = load_requirements(fixtures_dir)
    folders = []
    meta = load_folder_meta(fixtures_dir)
    if meta:
        folders.append(meta)

    output = tmp_path / "coverage_with_tests.xlsx"
    exporter = TestResultsExporter()
    exporter.export(reqs, folders, output)

    wb = load_workbook(str(output))
    ws = wb["Coverage"]

    coverage_map = {}
    verified_map = {}
    for row in ws.iter_rows(min_row=2, values_only=False):
        req_id = row[0].value
        coverage_map[req_id] = row[4].value
        verified_map[req_id] = row[2].value

    # E has tests → verified = Y
    assert verified_map.get("E") == "Y"
    # A has no tests → verified = N
    assert verified_map.get("A") == "N"


def test_test_results_formatting(fixtures_dir: Path, tmp_path: Path):
    reqs = load_requirements(fixtures_dir)
    folders = []
    meta = load_folder_meta(fixtures_dir)
    if meta:
        folders.append(meta)

    output = tmp_path / "results_fmt.xlsx"
    exporter = TestResultsExporter()
    exporter.export(reqs, folders, output)

    wb = load_workbook(str(output))
    ws_results = wb["Results"]
    ws_coverage = wb["Coverage"]

    # Header row is bold
    for cell in ws_results[1]:
        assert cell.font.bold is True
    for cell in ws_coverage[1]:
        assert cell.font.bold is True

    # Tab colours set
    assert ws_results.sheet_properties.tabColor is not None
    assert ws_coverage.sheet_properties.tabColor is not None
