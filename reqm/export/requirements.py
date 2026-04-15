"""Built-in exporter: flat requirements list as ECSS-styled Excel."""
from __future__ import annotations
from pathlib import Path

from openpyxl import Workbook

from reqm.export.base import AbstractExporter
from reqm.export._style import apply_header_style
from reqm.models import Requirement, FolderMeta, ValidationItem


_COLUMN_WIDTHS = {
    "A": 12,  # Is Folder
    "B": 16,  # ID
    "C": 16,  # Parent
    "D": 35,  # Title
    "E": 40,  # Description
    "F": 35,  # Rationale
    "G": 30,  # Acceptance Criteria
    "H": 16,  # Type
    "I": 25,  # Verification Method
    "J": 16,  # Derived From
    "K": 25,  # Related To
    "L": 20,  # Tags
    "M": 60,  # Path
}

_HEADERS = [
    "Is Folder", "ID", "Parent", "Title", "Description", "Rationale", "Acceptance Criteria",
    "Type", "Verification Method", "Derived From", "Related To", "Tags", "Path",
]


class RequirementsExporter(AbstractExporter):
    name = "requirements"
    description = "ECSS requirements list (one row per requirement)"

    def export(
        self,
        requirements: list[Requirement],
        folders: list[FolderMeta],
        items: list[ValidationItem],
        output: Path,
    ) -> None:
        """Write an ECSS requirements list workbook.

        Sheets produced:

        - **Requirements**: folders and requirements interleaved in a single
          sheet with columns ``Is Folder | ID | Parent | Title | Description |
          Rationale | Acceptance Criteria | Type | Verification Method |
          Derived From | Related To | Tags | Path``.
          Folder rows have ``Is Folder=TRUE``; requirement-only columns are
          blank. Requirement rows have ``Is Folder=FALSE``.

        Args:
            requirements: Full collection of validated requirements.
            folders: Folder metadata for all discovered folders.
            items: Loaded validation items (unused by this exporter).
            output: Destination path for the .xlsx file.
        """
        wb = Workbook()

        # Build path → folder ID lookup for parent resolution
        folder_id_by_path = {f.path: f.id for f in folders}

        ws = wb.active
        ws.title = "Requirements"
        ws.append(_HEADERS)

        for f in folders:
            parent_id = folder_id_by_path.get(f.path.parent, "")
            ws.append([
                True,
                f.id,
                parent_id,
                f.title,
                f.description,
                "", "", "", "", "", "", "",
                str(f.path),
            ])

        for req in requirements:
            parent_id = folder_id_by_path.get(req.path.parent, "")
            ws.append([
                False,
                req.id,
                parent_id,
                req.title,
                req.description,
                req.rationale,
                req.acceptance_criteria,
                req.type,
                ", ".join(req.verification),
                ", ".join(req.derived_from),
                ", ".join(req.related_to),
                ", ".join(req.tags),
                str(req.path),
            ])

        apply_header_style(ws, "4472C4")
        ws.auto_filter.ref = ws.dimensions

        for col_letter, width in _COLUMN_WIDTHS.items():
            ws.column_dimensions[col_letter].width = width

        wb.save(str(output))