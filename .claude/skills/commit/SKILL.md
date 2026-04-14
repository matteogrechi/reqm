---
name: commit
description: Commit staged or unstaged changes with a Conventional Commit message matching this repository's style. Use when the user asks to 'commit', 'commit changes', 'create a commit', 'save my work', or 'check in code'.
---

# Commit Changes

Create a well-structured commit following the Conventional Commits specification
already established in this repository.

## Guidelines

- **Never amend existing commits** without asking.
- **Never force-push or push** without explicit user approval.
- **Never skip pre-commit hooks** (do not use `--no-verify`).
- **Never skip signing commits** (do not use `--no-gpg-sign`).
- **Never use `git add .` or `git add -A`** — stage specific files only.
- Check for secrets or generated artefacts that should not be committed. If anything looks risky — ask.

## Workflow

### 1. Discover the current state

Run in parallel:

```
git status --short
git log --oneline -10
git diff HEAD
```

- If there are **no changes**, inform the user and stop.
- If there are **staged changes**, commit only those; do not stage unstaged changes.
- If there are **only unstaged changes**, stage all modified tracked files and proceed.

### 2. Group changes into logical clusters

Unrelated changes (e.g. a bug fix + a docs update) must become separate commits.
One cluster = one commit.

### 3. Draft the commit message

```
<type>[optional scope]: <description>

[optional body — what changed and why, not how]
```

**Types:** `feat` | `fix` | `docs` | `style` | `refactor` | `perf` | `test` | `build` | `ci` | `chore` | `revert`

Rules:
- Imperative mood — "add" not "added" or "adds"
- No capital letter at start; no trailing period
- Subject line ≤ 72 characters
- Body only when the change is non-obvious; explains *why*, not *how*

### 4. Present and confirm

Show the proposed commit(s) to the user. **Wait for explicit approval before executing.**

### 5. Execute

For each approved cluster, stage its files then commit:

```
git add <file1> <file2> ...
git commit -m "$(cat <<'EOF'
<subject>

<body>
EOF
)"
```

### 6. Confirm

```
git status --short
git log --oneline -1
```

If pre-commit hooks changed or blocked files — summarise what happened and ask
the user whether to stage and commit the follow-up edits.
