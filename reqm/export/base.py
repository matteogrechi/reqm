"""Abstract base class for all reqm export plugins."""
from __future__ import annotations
from abc import ABC, abstractmethod
from pathlib import Path
from reqm.models import Requirement, FolderMeta


class AbstractExporter(ABC):
    """Plugin contract for reqm exporters.

    To add a custom exporter:

    1. Create a module in reqm/export/ (or in your own package).
    2. Subclass AbstractExporter and set name + description.
    3. Implement export().
    4. Register via pyproject.toml entry point::

           [project.entry-points."reqm.exporters"]
           my-report = "my_package.my_module:MyExporter"

    The CLI discovers and registers all entry points automatically.

    Attributes:
        name: Subcommand name used in ``reqm export <name>``.
        description: One-line description shown in ``reqm export --help``.
    """

    name: str
    description: str

    @abstractmethod
    def export(
        self,
        requirements: list[Requirement],
        folders: list[FolderMeta],
        output: Path,
    ) -> None:
        """Write the report to the given output path.

        Args:
            requirements: Full collection of validated requirements.
            folders: Folder metadata for all discovered folders.
            output: Destination path for the report file.
        """
