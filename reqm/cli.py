"""CLI entry point."""
from __future__ import annotations
import sys
from pathlib import Path

import click

from reqm.fs import load_requirements, load_folder_meta
from reqm import validate as validate_mod
from reqm.export.base import AbstractExporter


class _ExportGroup(click.Group):
    """Export group that emits a custom error and exit 1 for unknown subcommands."""

    def invoke(self, ctx: click.Context) -> None:
        # Use protected_args (Click 8.x) or args (Click 9.x) for subcommand name
        import warnings
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            protected = ctx.protected_args
        subcmd = protected or ctx.args
        if subcmd and subcmd[0] not in self.commands:
            click.echo(f"Error: unknown exporter '{subcmd[0]}'", err=True)
            ctx.exit(1)
        return super().invoke(ctx)


@click.group()
def cli() -> None:
    """reqm — requirements manager."""


def _collect_folders(root: Path) -> list:
    """Walk root recursively and collect all FolderMeta objects."""
    from reqm.models import FolderMeta

    folders: list[FolderMeta] = []
    seen: set[Path] = set()
    for md_path in root.rglob(".folder-metadata.md"):
        parent = md_path.parent
        if parent not in seen:
            seen.add(parent)
            meta = load_folder_meta(parent)
            if meta is not None:
                folders.append(meta)
    return folders


def _register_exporters(export_group: click.Group) -> None:
    """Load reqm.exporters entry points and wrap each as a click.Command."""
    import importlib.metadata as importlib_metadata

    eps = importlib_metadata.entry_points(group="reqm.exporters")
    for ep in eps:
        exporter_cls = ep.load()
        instance: AbstractExporter = exporter_cls()

        @click.command(name=instance.name, help=instance.description)
        @click.option("--output", "-o", default=None, help="Output file path")
        @click.option("--root", default="requirements", show_default=True)
        def _export_cmd(root: str, output: str | None, _exporter=instance) -> None:
            reqs = load_requirements(Path(root))
            folders = _collect_folders(Path(root))
            if output is None:
                output = f"{_exporter.name}.xlsx"
            _exporter.export(reqs, folders, [], Path(output))

        export_group.add_command(_export_cmd)


@cli.command()
@click.option("--folder", default=None, help="Filter by folder ID")
@click.option("--status", default=None, help="Filter by status")
@click.option("--root", default="requirements", show_default=True)
def list(folder: str | None, status: str | None, root: str) -> None:
    """List requirements."""
    reqs = load_requirements(Path(root))
    folders = _collect_folders(Path(root))
    folder_map = {f.id: f for f in folders}

    # Build a lookup: requirement file path → folder id
    req_folder: dict[Path, str] = {}
    for f in folders:
        for r in reqs:
            try:
                r.path.relative_to(f.path)
                req_folder[r.path] = f.id
            except ValueError:
                continue

    if folder is not None:
        reqs = [r for r in reqs if req_folder.get(r.path) == folder]
    if status is not None:
        reqs = [r for r in reqs if r.status == status]

    click.echo(
        f"{'ID':<15} {'Title':<35} {'Type':<15} {'Verification':<25} {'Folder ID':<15}"
    )
    click.echo("-" * 105)
    for r in reqs:
        ver = ", ".join(r.verification) if r.verification else ""
        fid = req_folder.get(r.path, "")
        click.echo(f"{r.id:<15} {r.title:<35} {r.type:<15} {ver:<25} {fid:<15}")


@cli.command()
@click.argument("req_id")
@click.option("--root", default="requirements", show_default=True)
def show(req_id: str, root: str) -> None:
    """Display a single requirement."""
    reqs = load_requirements(Path(root))
    target = None
    for r in reqs:
        if r.id == req_id:
            target = r
            break

    if target is None:
        click.echo(f"Error: requirement '{req_id}' not found.", err=True)
        sys.exit(1)

    click.echo(f"ID:                  {target.id}")
    click.echo(f"Title:               {target.title}")
    click.echo(f"Type:                {target.type}")
    click.echo(f"Verification:        {', '.join(target.verification) if target.verification else ''}")
    if target.derived_from:
        click.echo(f"Derived From:        {', '.join(target.derived_from)}")
    if target.related_to:
        click.echo(f"Related To:          {', '.join(target.related_to)}")
    if target.tags:
        click.echo(f"Tags:                {', '.join(target.tags)}")
    if target.priority:
        click.echo(f"Priority:            {target.priority}")
    if target.status:
        click.echo(f"Status:              {target.status}")
    if target.stability:
        click.echo(f"Stability:           {target.stability}")
    if target.description:
        click.echo(f"\nDescription:\n{target.description}")
    if target.rationale:
        click.echo(f"\nRationale:\n{target.rationale}")
    if target.acceptance_criteria:
        click.echo(f"\nAcceptance Criteria:\n{target.acceptance_criteria}")


@cli.command()
@click.option("--root", default="requirements", show_default=True)
def validate(root: str) -> None:
    """Validate all requirements. Exits non-zero on errors."""
    reqs = load_requirements(Path(root))
    errors = validate_mod.validate(reqs)
    if errors:
        for e in errors:
            click.echo(f"[{e.req_id}] {e.message}")
        sys.exit(1)
    else:
        click.echo("All requirements valid.")
        sys.exit(0)


@cli.group(cls=_ExportGroup)
def export() -> None:
    """Export requirements to a report."""


_register_exporters(export)
cli.add_command(export)