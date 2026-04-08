# Commit Skill

## Purpose
Generate well-structured git commit messages following Conventional Commit best practices.

## Workflow

1. **Gather context** — Run:
   ```
   git status && git diff HEAD && git log -n 5 --oneline
   ```
   Review all staged and unstaged changes, plus recent commit history.

2. **Cluster changes by affinity** — Group modified files into logical clusters:
   - Files changed for the same reason or feature belong together
   - Unrelated changes (e.g., a bugfix + a refactor + a docs update) should be split into separate commit groups
   - Prefer small, focused commits over large monolithic ones

3. **Propose commit messages** — For each cluster, draft a Conventional Commit message:
   ```
   <type>[optional scope]: <description>

   [optional body]
   ```
   **Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`

   **Rules**:
   - Use imperative mood in the subject ("add" not "added" / "adds")
   - No capitalization at the start of the subject line
   - No trailing period in the subject line
   - Keep subject line ≤ 72 characters
   - Use the body to explain *what* and *why* (not *how*) when the change is non-obvious

4. **Ask for confirmation** — Present the proposed commit(s) to the user and wait for approval before executing.

5. **Execute** — Stage only the files belonging to the approved cluster and run `git commit -m "<message>"`.
