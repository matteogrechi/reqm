"""Domain models for requirements and folder metadata."""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class FolderMeta:
    """Parsed from .folder-metadata.md in each requirements folder."""
    path: Path
    id: str
    title: str
    description: str = ""                 # body of the .folder-metadata.md file
    extra: dict = field(default_factory=dict)


@dataclass
class Requirement:
    """Parsed from a requirement markdown file."""
    path: Path
    id: str
    title: str
    description: str = ""                 # ## Description section of the body
    rationale: str = ""                   # ## Rationale section of the body
    acceptance_criteria: str = ""         # ## Acceptance Criteria section of the body
    type: str = "Functional"
    verification: list[str] = field(default_factory=list)  # Test | Analysis | Inspection | Demonstration
    tags: list[str] = field(default_factory=list)
    derived_from: str | None = None        # relationships.derived_from in frontmatter
    related_to: list[str] = field(default_factory=list)  # relationships.related_to in frontmatter
    priority: str | None = None
    status: str | None = None
    stability: str | None = None
    tests: list[str] = field(default_factory=list)
    extra: dict = field(default_factory=dict)
