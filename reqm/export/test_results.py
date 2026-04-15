"""Built-in exporter: validation plan as ECSS-styled Excel."""
from __future__ import annotations
from pathlib import Path

from openpyxl import Workbook

from reqm.export.base import AbstractExporter
from reqm.export._style import apply_header_style
from reqm.models import Requirement, FolderMeta, ValidationItem


class TestResultsExporter(AbstractExporter):
    name = "test-results"
    description = "ECSS validation plan and coverage report"

    def export(
        self,
        requirements: list[Requirement],
        folders: list[FolderMeta],
        items: list[ValidationItem],
        output: Path,
    ) -> None:
        """Write an ECSS validation plan workbook.

        Sheets produced:

        - **Results**: one row per linked validation item — Req ID, Item ID,
          Item Title. Populated by resolving each ``validated_by`` ID against
          the loaded ``ValidationItem`` collection.
        - **Coverage**: one row per requirement — Req ID, Title, Verified
          (Y/N), Verification Method, Item Count.

        Args:
            requirements: Full collection of validated requirements.
            folders: Folder metadata for all discovered folders.
            items: Loaded validation items used to resolve titles.
            output: Destination path for the .xlsx file.
        """
        wb = Workbook()
        item_by_id = {item.id: item for item in items}

        # --- Results sheet ---
        ws_results = wb.active
        ws_results.title = "Results"
        ws_results.append(["Req ID", "Item ID", "Item Title"])

        for req in requirements:
            for item_id in req.validated_by:
                item = item_by_id.get(item_id)
                title = item.title if item else ""
                ws_results.append([req.id, item_id, title])

        apply_header_style(ws_results, "4472C4")
        ws_results.column_dimensions["A"].width = 16
        ws_results.column_dimensions["B"].width = 16
        ws_results.column_dimensions["C"].width = 40

        # --- Coverage sheet ---
        ws_coverage = wb.create_sheet("Coverage")
        ws_coverage.append(["Req ID", "Title", "Verified (Y/N)", "Verification Method", "Item Count"])

        for req in requirements:
            item_count = len(req.validated_by)
            verified = "Y" if item_count > 0 else "N"
            ws_coverage.append([
                req.id,
                req.title,
                verified,
                ", ".join(req.verification),
                item_count,
            ])

        apply_header_style(ws_coverage, "70AD47")
        ws_coverage.column_dimensions["A"].width = 16
        ws_coverage.column_dimensions["B"].width = 35
        ws_coverage.column_dimensions["C"].width = 16
        ws_coverage.column_dimensions["D"].width = 25
        ws_coverage.column_dimensions["E"].width = 14

        wb.save(str(output))