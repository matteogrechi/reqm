"""Tests for reqm.cli — all commands via CliRunner."""
from pathlib import Path

import pytest
from click.testing import CliRunner
from reqm.cli import cli


def test_list_all(fixtures_dir: Path):
    runner = CliRunner()
    result = runner.invoke(cli, ["list", "--root", str(fixtures_dir)])
    assert result.exit_code == 0
    assert "A" in result.output
    assert "B" in result.output


def test_list_filter_folder(fixtures_dir: Path):
    runner = CliRunner()
    result = runner.invoke(cli, ["list", "--root", str(fixtures_dir), "--folder", "NONEXISTENT"])
    assert result.exit_code == 0
    # Should have headers but no data rows
    assert "ID" in result.output


def test_show_found(fixtures_dir: Path):
    runner = CliRunner()
    result = runner.invoke(cli, ["show", "A", "--root", str(fixtures_dir)])
    assert result.exit_code == 0
    assert "Parent requirement" in result.output
    assert "Functional" in result.output


def test_show_not_found(fixtures_dir: Path):
    runner = CliRunner()
    result = runner.invoke(cli, ["show", "NOPE", "--root", str(fixtures_dir)])
    assert result.exit_code == 1
    assert "not found" in result.output


def test_validate_success(fixtures_dir: Path):
    runner = CliRunner()
    result = runner.invoke(cli, ["validate", "--root", str(fixtures_dir)])
    assert result.exit_code == 0
    assert "All requirements valid." in result.output


def test_export_requirements_creates_file(tmp_path: Path, fixtures_dir: Path):
    runner = CliRunner()
    output = str(tmp_path / "reqs.xlsx")
    result = runner.invoke(cli, ["export", "requirements", "--root", str(fixtures_dir), "-o", output])
    assert result.exit_code == 0
    assert (tmp_path / "reqs.xlsx").exists()


def test_export_traceability_creates_file(tmp_path: Path, fixtures_dir: Path):
    runner = CliRunner()
    output = str(tmp_path / "trace.xlsx")
    result = runner.invoke(cli, ["export", "traceability", "--root", str(fixtures_dir), "-o", output])
    assert result.exit_code == 0
    assert (tmp_path / "trace.xlsx").exists()


def test_export_test_results_creates_file(tmp_path: Path, fixtures_dir: Path):
    runner = CliRunner()
    output = str(tmp_path / "tests.xlsx")
    result = runner.invoke(cli, ["export", "test-results", "--root", str(fixtures_dir), "-o", output])
    assert result.exit_code == 0
    assert (tmp_path / "tests.xlsx").exists()


def test_export_unknown_exporter(fixtures_dir: Path):
    runner = CliRunner()
    result = runner.invoke(cli, ["export", "nonexistent", "--root", str(fixtures_dir)])
    assert result.exit_code == 1
    assert "unknown exporter" in result.output


def test_export_help_lists_exporters():
    runner = CliRunner()
    result = runner.invoke(cli, ["export", "--help"])
    assert result.exit_code == 0
    assert "requirements" in result.output
    assert "traceability" in result.output
    assert "test-results" in result.output
