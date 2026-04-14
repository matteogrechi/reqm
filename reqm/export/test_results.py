"""Built-in exporter: test results as ECSS-styled Excel."""
from __future__ import annotations
from pathlib import Path

from openpyxl import Workbook

from reqm.export.base import AbstractExporter
from reqm.export._style import apply_header_style
from reqm.models import Requirement, FolderMeta


class TestResultsExporter(AbstractExporter):
    name = "test-results"
    description = "ECSS test results and coverage report"

    def export(
        self,
        requirements: list[Requirement],
        folders: list[FolderMeta],
        output: Path,
    ) -> None:
        """Write an ECSS test results workbook.

        Sheets produced:

        - **Results**: Req ID, Test ID, Test Title, Result, Date, Notes.
        - **Coverage**: Req ID, Title, Verified (Y/N), Method, Coverage %.

        Test outcome data is read from files referenced in requirement
        frontmatter under the ``validated_by`` key.

        Args:
            requirements: Full collection of validated requirements.
            folders: Folder metadata for all discovered folders.
            output: Destination path for the .xlsx file.
        """
        wb = Workbook()

        # --- Results sheet ---
        ws_results = wb.active
        ws_results.title = "Results"
        ws_results.append(["Req ID", "Test ID", "Test Title", "Result", "Date", "Notes"])

        # TODO: EXP-013 pending — test file format not yet specified
        for req in requirements:
            for test_id in req.validated_by:
                ws_results.append([req.id, test_id, "", "", "", ""])

        apply_header_style(ws_results, "4472C4")
        ws_results.column_dimensions["A"].width = 16
        ws_results.column_dimensions["B"].width = 16
        ws_results.column_dimensions["C"].width = 35
        ws_results.column_dimensions["D"].width = 12
        ws_results.column_dimensions["E"].width = 14
        ws_results.column_dimensions["F"].width = 30

        # --- Coverage sheet ---
        ws_coverage = wb.create_sheet("Coverage")
        ws_coverage.append(["Req ID", "Title", "Verified (Y/N)", "Method", "Coverage %"])

        for req in requirements:
            total = len(req.validated_by) if req.validated_by else 0
            if total > 0:
                # TODO: EXP-013 pending — test file format not yet specified
                passed = 0
                coverage = round(passed / total * 100, 2)
                verified = "Y"
            else:
                coverage = 0
                verified = "N"

            ws_coverage.append([
                req.id,
                req.title,
                verified,
                ", ".join(req.verification),
                coverage,
            ])

        apply_header_style(ws_coverage, "70AD47")
        ws_coverage.column_dimensions["A"].width = 16
        ws_coverage.column_dimensions["B"].width = 35
        ws_coverage.column_dimensions["C"].width = 16
        ws_coverage.column_dimensions["D"].width = 25
        ws_coverage.column_dimensions["E"].width = 14

        wb.save(str(output))
