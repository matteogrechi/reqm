"""File system helpers: discover and parse requirement markdown files."""
from __future__ import annotations
import yaml
from pathlib import Path
from reqm.models import Requirement, FolderMeta


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

    known_keys = {"id", "title", "description"}
    extra = {k: v for k, v in data.items() if k not in known_keys}

    return FolderMeta(
        path=path.parent,
        id=data.get("id", ""),
        title=data.get("title", ""),
        description=data.get("description", ""),
        extra=extra,
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
    validated_by = rel.get("validated_by", []) or []

    known_keys = {
        "id", "title", "type", "verification", "tags",
        "derived_from", "related_to", "relationships",
        "priority", "status", "stability",
        "description", "rationale", "acceptance_criteria",
    }
    extra = {k: v for k, v in data.items() if k not in known_keys}

    return Requirement(
        path=path,
        id=data.get("id", ""),
        title=data.get("title", ""),
        description=sections.get("Description", ""),
        rationale=sections.get("Rationale", ""),
        acceptance_criteria=sections.get("Acceptance Criteria", ""),
        type=data.get("type", "Functional"),
        verification=data.get("verification", []) or [],
        tags=data.get("tags", []) or [],
        derived_from=derived_from,
        related_to=related_to or [],
        priority=data.get("priority"),
        status=data.get("status"),
        stability=data.get("stability"),
        validated_by=validated_by,
        extra=extra,
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
