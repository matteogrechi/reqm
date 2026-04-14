"""Built-in exporter: flat requirements list as ECSS-styled Excel."""
from __future__ import annotations
from pathlib import Path

from openpyxl import Workbook
from openpyxl.utils import get_column_letter

from reqm.export.base import AbstractExporter
from reqm.export._style import apply_header_style
from reqm.models import Requirement, FolderMeta

_COLUMN_WIDTHS = {
    "A": 16,  # ID
    "B": 35,  # Title
    "C": 40,  # Description
    "D": 35,  # Rationale
    "E": 30,  # Acceptance Criteria
    "F": 16,  # Type
    "G": 25,  # Verification Method
    "H": 16,  # Derived From
    "I": 25,  # Related To
    "J": 20,  # Tags
    "K": 15,  # Folder ID
}

_HEADERS = [
    "ID", "Title", "Description", "Rationale", "Acceptance Criteria",
    "Type", "Verification Method", "Derived From", "Related To", "Tags", "Folder ID",
]


class RequirementsExporter(AbstractExporter):
    name = "requirements"
    description = "ECSS requirements list (one row per requirement)"

    def export(
        self,
        requirements: list[Requirement],
        folders: list[FolderMeta],
        output: Path,
    ) -> None:
        """Write an ECSS requirements list workbook.

        Sheets produced:

        - **Requirements**: ID, Title, Description, Rationale, Acceptance
          Criteria, Type, Verification, Derived From, Related To, Tags, Folder.
        - **Folders**: ID, Title, Description.

        Args:
            requirements: Full collection of validated requirements.
            folders: Folder metadata for all discovered folders.
            output: Destination path for the .xlsx file.
        """
        wb = Workbook()

        # --- Requirements sheet ---
        ws_req = wb.active
        ws_req.title = "Requirements"
        ws_req.append(_HEADERS)

        for req in requirements:
            ws_req.append([
                req.id,
                req.title,
                req.description,
                req.rationale,
                req.acceptance_criteria,
                req.type,
                ", ".join(req.verification),
                ", ".join(req.derived_from),
                ", ".join(req.related_to),
                ", ".join(req.tags),
                "",  # Folder ID filled in by a later pass if needed
            ])

        apply_header_style(ws_req, "4472C4")
        ws_req.auto_filter.ref = ws_req.dimensions

        for col_letter, width in _COLUMN_WIDTHS.items():
            ws_req.column_dimensions[col_letter].width = width

        # --- Folders sheet ---
        ws_folders = wb.create_sheet("Folders")
        ws_folders.append(["ID", "Title", "Description"])
        for f in folders:
            ws_folders.append([f.id, f.title, f.description])

        apply_header_style(ws_folders, "70AD47")
        ws_folders.auto_filter.ref = ws_folders.dimensions
        ws_folders.column_dimensions["A"].width = 15
        ws_folders.column_dimensions["B"].width = 35
        ws_folders.column_dimensions["C"].width = 50

        wb.save(str(output))
