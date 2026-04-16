"""File system helpers: discover and parse requirement and validation item files."""
from __future__ import annotations
import yaml
from pathlib import Path
from reqm.models import Requirement, FolderMeta, SpecMeta, RelatedSpecification, ValidationItem


def _split_frontmatter(text: str) -> tuple[str, str]:
    """Split markdown text into (yaml_frontmatter, markdown_body).

    Expects the file to start with ``---`` on the first line, followed by
    YAML metadata, then a closing ``---``.  Everything after the closing
    delimiter is returned as the body.

    Args:
        text: Full text of a markdown file.

    Returns:
        Tuple of (yaml string, remaining markdown body).
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return "", text

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        return "", text

    yaml_text = "\n".join(lines[1:end_idx])
    body = "\n".join(lines[end_idx + 1:])
    return yaml_text, body


def _extract_sections(body: str) -> dict[str, str]:
    """Parse markdown body into a dict of ``## Heading`` → section text.

    Lines before the first ``##`` heading are stored under the ``""`` key.

    Args:
        body: Markdown text after frontmatter.

    Returns:
        Mapping of section heading (without ``##``) to its content.
    """
    sections: dict[str, str] = {"": ""}
    current_heading = ""

    for line in body.splitlines():
        if line.startswith("## "):
            current_heading = line[3:].strip()
            sections[current_heading] = ""
        else:
            sections[current_heading] += line + "\n"

    # Strip trailing newlines from each section
    return {k: v.rstrip() for k, v in sections.items()}


def parse_folder_meta(path: Path) -> FolderMeta:
    """Parse a single .folder-metadata.md file with YAML frontmatter.

    Args:
        path: Path to the .folder-metadata.md file.

    Returns:
        Parsed FolderMeta dataclass.
    """
    text = path.read_text(encoding="utf-8")
    yaml_text, body = _split_frontmatter(text)
    data = yaml.safe_load(yaml_text) or {}
    sections = _extract_sections(body)

    return FolderMeta(
        path=path.parent,
        id=data.get("id", ""),
        title=data.get("title", ""),
        description=sections.get("Description", "").strip("\n"),
    )


def parse_requirement(path: Path) -> Requirement:
    """Parse a single requirement markdown file with YAML frontmatter.

    Body sections ``## Description``, ``## Rationale``, and
    ``## Acceptance Criteria`` are extracted and mapped to fields.
    Any unrecognised frontmatter keys are stored in ``extra`` and will
    produce a validation error when ``validate()`` is called.

    Args:
        path: Path to the requirement .md file.

    Returns:
        Parsed Requirement dataclass.
    """
    text = path.read_text(encoding="utf-8")
    yaml_text, body = _split_frontmatter(text)
    data = yaml.safe_load(yaml_text) or {}
    sections = _extract_sections(body)

    # relationships sub-dict
    rel = data.get("relationships", {}) or {}
    _df_raw = rel.get("derived_from") or data.get("derived_from")
    derived_from = [_df_raw] if isinstance(_df_raw, str) else (_df_raw or [])
    related_to = rel.get("related_to", []) or data.get("related_to", [])
    validated_by_raw = rel.get("validated_by", []) or []
    validated_by = [str(v) for v in validated_by_raw]

    return Requirement(
        path=path,
        id=data.get("id", ""),
        title=data.get("title", ""),
        description=sections.get("Description", "").strip("\n"),
        rationale=sections.get("Rationale", "").strip("\n"),
        acceptance_criteria=sections.get("Acceptance Criteria", "").strip("\n"),
        type=data.get("type", "Functional"),
        verification=data.get("verification", []) or [],
        tags=data.get("tags", []) or [],
        derived_from=derived_from,
        related_to=related_to or [],
        priority=data.get("priority"),
        status=data.get("status"),
        stability=data.get("stability"),
        validated_by=validated_by,
    )


def parse_validation_item(path: Path) -> ValidationItem:
    """Parse a single validation item markdown file with YAML frontmatter.

    Body sections ``## Objective``, ``## Preconditions``, ``## Procedure``,
    and ``## Pass Criteria`` are extracted and mapped to fields.

    Args:
        path: Path to the validation item .md file.

    Returns:
        Parsed ValidationItem dataclass.
    """
    text = path.read_text(encoding="utf-8")
    yaml_text, body = _split_frontmatter(text)
    data = yaml.safe_load(yaml_text) or {}
    sections = _extract_sections(body)

    rel = data.get("relationships", {}) or {}
    _df_raw = rel.get("derived_from") or data.get("derived_from")
    derived_from = [_df_raw] if isinstance(_df_raw, str) else (_df_raw or [])
    related_to = rel.get("related_to", []) or data.get("related_to", [])

    return ValidationItem(
        path=path,
        id=data.get("id", ""),
        title=data.get("title", ""),
        method=data.get("method", ""),
        level=data.get("level", ""),
        status=data.get("status"),
        priority=data.get("priority"),
        stability=data.get("stability"),
        tags=data.get("tags", []) or [],
        derived_from=derived_from,
        related_to=related_to or [],
        objective=sections.get("Objective", "").strip("\n"),
        preconditions=sections.get("Preconditions", "").strip("\n"),
        procedure=sections.get("Procedure", "").strip("\n"),
        pass_criteria=sections.get("Pass Criteria", "").strip("\n"),
    )


def load_folder_meta(folder: Path) -> FolderMeta | None:
    """Parse .folder-metadata.md in the given folder, or return None if absent.

    Args:
        folder: Directory that may contain a .folder-metadata.md file.

    Returns:
        Parsed FolderMeta, or None if no .folder-metadata.md is present.
    """
    meta_path = folder / ".folder-metadata.md"
    if not meta_path.exists():
        return None
    return parse_folder_meta(meta_path)


def find_spec_root(start: Path) -> Path:
    """Walk upward from start to find the directory containing .specification-metadata.md.

    At each directory, checks that neither .project-metadata.md nor .folder-metadata.md
    coexist with .specification-metadata.md, and raises if any incompatible pair is found.

    Args:
        start: Directory to begin the upward search from.

    Returns:
        First ancestor directory (inclusive of start) containing .specification-metadata.md.

    Raises:
        FileNotFoundError: When no .specification-metadata.md is found before the filesystem root.
        RuntimeError: When .specification-metadata.md coexists with .project-metadata.md or .folder-metadata.md.
    """
    current = start.resolve()
    while True:
        spec = current / ".specification-metadata.md"
        legacy = current / ".project-metadata.md"
        folder = current / ".folder-metadata.md"
        if spec.exists() and legacy.exists():
            raise RuntimeError(
                f"Both .specification-metadata.md and .project-metadata.md exist in {current}; "
                "remove one before proceeding."
            )
        if spec.exists() and folder.exists():
            raise RuntimeError(
                f"Both .specification-metadata.md and .folder-metadata.md exist in {current}; "
                "a directory cannot be both a specification root and a folder."
            )
        if spec.exists():
            return current
        parent = current.parent
        if parent == current:
            raise FileNotFoundError(
                f"No .specification-metadata.md found in {start} or any parent directory."
            )
        current = parent


def load_spec_meta(root: Path) -> SpecMeta:
    """Parse .specification-metadata.md from the given root directory.

    Reads the YAML frontmatter and builds a ``SpecMeta`` instance.
    If the file is absent, returns a default instance with empty values.

    Args:
        root: Directory that may contain a .specification-metadata.md file.

    Returns:
        Parsed SpecMeta (never None).
    """
    meta_path = root / ".specification-metadata.md"
    if not meta_path.exists():
        return SpecMeta(path=root)

    text = meta_path.read_text(encoding="utf-8")
    yaml_text, body = _split_frontmatter(text)
    data = yaml.safe_load(yaml_text) or {}
    sections = _extract_sections(body)

    related_specifications: list[RelatedSpecification] = []
    for entry in data.get("related_specifications", []) or []:
        related_specifications.append(
            RelatedSpecification(
                id=entry.get("id", ""),
                local_path=entry.get("local_path", ""),
            )
        )

    return SpecMeta(
        path=root,
        id=data.get("id", ""),
        title=data.get("title", ""),
        description=sections.get("Description", "").strip("\n"),
        type=data.get("type", "requirements"),
        related_specifications=related_specifications,
    )


def load_validation_items(root: Path) -> list[ValidationItem]:
    """Recursively discover and parse all validation item files under root.

    Skips dotfiles and files without YAML frontmatter.

    Args:
        root: Directory to search for validation item markdown files.

    Returns:
        All parsed validation items found under root, in discovery order.
    """
    items: list[ValidationItem] = []
    for md_path in sorted(root.rglob("*.md")):
        if md_path.name == ".folder-metadata.md":
            continue
        if md_path.name.startswith("."):
            continue
        text = md_path.read_text(encoding="utf-8")
        first_line = text.splitlines()[0].strip() if text.splitlines() else ""
        if first_line != "---":
            continue
        items.append(parse_validation_item(md_path))
    return items


def load_requirements(root: Path) -> list[Requirement]:
    """Recursively discover and parse all requirement files under root.

    Skips ``.folder-metadata.md`` files, dotfiles, and files without
    YAML frontmatter (i.e. not starting with ``---``).

    Args:
        root: Directory to search for requirement markdown files.

    Returns:
        All parsed requirements found under root, in discovery order.
    """
    reqs: list[Requirement] = []
    for md_path in sorted(root.rglob("*.md")):
        if md_path.name == ".folder-metadata.md":
            continue
        if md_path.name.startswith("."):
            continue
        # Skip files without YAML frontmatter
        text = md_path.read_text(encoding="utf-8")
        first_line = text.splitlines()[0].strip() if text.splitlines() else ""
        if first_line != "---":
            continue
        reqs.append(parse_requirement(md_path))
    return reqs