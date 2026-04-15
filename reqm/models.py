"""Domain models for requirements, validation items, and folder metadata."""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class RelatedProject:
    """A project related to the current one, used for cross-project traceability."""
    id: str
    title: str
    local_path: str = ""


@dataclass
class ProjectMeta:
    """Parsed from .project-metadata.md in the requirements root."""
    path: Path
    project_key: str = ""
    validation_items_path: str = ""
    related_projects: list[RelatedProject] = field(default_factory=list)


@dataclass
class FolderMeta:
    """Parsed from .folder-metadata.md in each requirements folder."""
    path: Path
    id: str
    title: str
    description: str = ""                 # body of the .folder-metadata.md file
    extra: dict = field(default_factory=dict)


@dataclass
class ValidationItem:
    """Parsed from a validation item markdown file."""
    path: Path
    id: str
    title: str
    method: str = ""               # Test | Analysis | Inspection | Demonstration
    level: str = ""                # Unit | Integration | System | Acceptance
    status: str | None = None
    priority: str | None = None
    stability: str | None = None
    tags: list[str] = field(default_factory=list)
    derived_from: list[str] = field(default_factory=list)
    related_to: list[str] = field(default_factory=list)
    objective: str = ""
    preconditions: str = ""
    procedure: str = ""
    pass_criteria: str = ""
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
    derived_from: list[str] = field(default_factory=list)  # relationships.derived_from in frontmatter
    related_to: list[str] = field(default_factory=list)    # relationships.related_to in frontmatter
    priority: str | None = None
    status: str | None = None
    stability: str | None = None
    validated_by: list[str] = field(default_factory=list)  # plain IDs — resolved against ValidationItem collection
    extra: dict = field(default_factory=dict)