# reqm — Agent Guidelines

## What this project is

`reqm` is a minimal, read-only CLI for managing software requirements stored as
Markdown files with YAML frontmatter. It validates them and exports ECSS-compliant
Excel reports. It never writes requirement files — the user owns those.

## Source of truth

**Read `FUN-reqm-product-requirements/` before every coding session.**
All functional behaviour, CLI commands, and export formats are specified there.
When requirements change, update code and docs to match. Do not implement anything
not covered by requirements without asking first.

## Absolute invariants — never violate these

- The tool never creates, edits, or deletes files inside `FUN-reqm-product-requirements/`
- `AbstractExporter` in `reqm/export/base.py` is the sole plugin contract;
  all exporters must subclass it and nothing else
- All exporters are discovered via `reqm.exporters` entry points — the CLI
  must not hard-code exporter names
- `reqm validate` must exit non-zero when any `ValidationError` is returned

## Module responsibilities

| Module | Responsibility |
|---|---|
| `reqm/models.py` | Dataclasses only — no I/O, no business logic |
| `reqm/fs.py` | Discover and parse `.md` files — no validation, no export |
| `reqm/validate.py` | Validation rules only — pure functions, no I/O |
| `reqm/cli.py` | Wire commands to fs + validate + exporters — no business logic |
| `reqm/export/base.py` | Plugin contract — do not add methods without a requirement |
| `reqm/export/*.py` | One exporter per file — no cross-dependencies between exporters |

## Skills

Skills are auto-invoked by the harness based on their trigger conditions. They can
also be loaded explicitly with the Skill tool:

- Touching `reqm/export/` or adding an exporter → `/exporter` (`.claude/skills/exporter/SKILL.md`)
- Touching `reqm/models.py` or any frontmatter schema → `/models` (`.claude/skills/models/SKILL.md`)
- Touching `reqm/validate.py` → `/validate` (`.claude/skills/validate/SKILL.md`)
- Rewriting or auditing any requirement file → `/incose-rewrite` (`.claude/skills/incose-rewrite/SKILL.md`)
- Committing changes → `/commit` (`.claude/skills/commit/SKILL.md`)

## Tooling

Use `uv` for all Python tool invocations — never call `python`, `pip`, or `pytest` directly:

```sh
uv run pytest
uv run reqm validate <path>
```

## Workflow

1. Read all files under `FUN-reqm-product-requirements/`
2. Diff requirements against current implementation
3. Implement what is missing or changed
4. Update `docs/` to reflect the current state
5. Run `uv run pytest` — fix until green
6. Run `uv run reqm validate` on the sample requirements — fix until clean

## Code style

Follow the **antirez style** (Salvatore Sanfilippo / Redis codebase):

- Write for the reader, not the machine — clarity always beats cleverness
- Flat is better than nested — early returns, no deep indentation pyramids
- Short, single-purpose functions — if you need to explain what a function does with more than one sentence, split it
- No defensive checks on internal inputs — trust your own code; validate only at system boundaries
- Name things precisely but briefly — avoid noise words (`data`, `info`, `manager`, `helper`)
- Comments explain *why*, never *what* — if the what needs a comment, simplify the code instead
- No speculative abstractions — only introduce indirection when a second concrete use case exists

Additional Python conventions:

- Python 3.14+, typed, `from __future__ import annotations`
- No print statements in library code — use `click.echo` only in `cli.py`
- Docstrings on every public function and class — Google style
- All imports at the top of the file — no inline or deferred imports
- No nested functions; no inner/helper functions defined inside other functions
