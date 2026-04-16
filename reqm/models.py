"""Domain models for requirements, validation items, and folder metadata."""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal


ReqType = Literal["Functional", "Performance", "Interface", "Constraint"]
VerificationMethod = Literal["Test", "Analysis", "Inspection", "Demonstration"]
Priority = Literal["High", "Medium", "Low"]
Stability = Literal["Volatile", "Evolving", "Stable"]
SpecContentType = Literal["requirements", "validation_items"]


@dataclass
class RelatedSpecification:
    """A specification related to the current one, used for cross-specification traceability."""
    id: str
    local_path: str = ""


@dataclass
class SpecMeta:
    """Parsed from .specification-metadata.md in the specification root."""
    path: Path
    id: str = ""
    title: str = ""
    description: str = ""
    type: SpecContentType = "requirements"
    related_specifications: list[RelatedSpecification] = field(default_factory=list)


@dataclass
class FolderMeta:
    """Parsed from .folder-metadata.md in each requirements folder."""
    path: Path
    id: str
    title: str
    description: str = ""


@dataclass
class ValidationItem:
    """Parsed from a validation item markdown file."""
    path: Path
    id: str
    title: str
    method: VerificationMethod | None = None
    level: str = ""
    status: str | None = None
    priority: Priority | None = None
    stability: Stability | None = None
    tags: list[str] = field(default_factory=list)
    derived_from: list[str] = field(default_factory=list)
    related_to: list[str] = field(default_factory=list)
    objective: str = ""
    preconditions: str = ""
    procedure: str = ""
    pass_criteria: str = ""


@dataclass
class Requirement:
    """Parsed from a requirement markdown file."""
    path: Path
    id: str
    title: str
    description: str = ""
    rationale: str = ""
    acceptance_criteria: str = ""
    type: ReqType = "Functional"
    verification: list[VerificationMethod] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    derived_from: list[str] = field(default_factory=list)
    related_to: list[str] = field(default_factory=list)
    priority: Priority | None = None
    status: str | None = None
    stability: Stability | None = None
    validated_by: list[str] = field(default_factory=list)
