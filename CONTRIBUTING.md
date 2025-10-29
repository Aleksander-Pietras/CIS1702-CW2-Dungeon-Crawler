# CONTRIBUTING

Hello my beloved team, please appreciate this file as it took me forever to make, (before anyone asks, yes ChatGPT has been used in some areas when writing this, if you are curious I listed everything ChatGPT did for me at the bottom of the document)

This document explains the project, shows how to install, configure and run it, and communicates important context and collaboration tips.

---

## Table of contents

* Quick start (clone & run)
* Setting up Git & GitHub
* Useful Git commands (cheat sheet)
* Python style & syntax rules
* Helpful tips and etiquette

---

## Quick start (clone & run)

Open Git Bash and navigate to the folder where you want to keep the project. Then clone the repository.

**Clone (SSH)** - recommended if you have an SSH key configured:

```bash
git clone git@github.com:Aleksander-Pietras/CIS1702-CW2-Dungeon-Crawler.git
```

**Clone (HTTPS)** - useful on shared machines or if you prefer password/token entry:

```bash
git clone https://github.com/Aleksander-Pietras/CIS1702-CW2-Dungeon-Crawler.git
```

Open the project folder:

```bash
cd CIS1702-CW2-Dungeon-Crawler
```

You should now see `(main)` (or the default branch name) at the end of your prompt in Git Bash.

Tip: use wildcard completion to save typing, e.g. `cd CIS*` or `cd C*` - your shell will expand it.

---

## Setting up Git & GitHub

### 1. Configure Git (first time)

Set your name and email (these are used in commit metadata):

```bash
git config --global user.name "Your Name"
git config --global user.email your.email@example.com
```

Check your configuration:

```bash
git config --list
```

### 2. SSH key

Generate a new SSH key if you don't already have one:

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
# or, if ed25519 not available:
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
```

Then add the public key (`~/.ssh/id_ed25519.pub` or `~/.ssh/id_rsa.pub`) to your GitHub account (Settings → SSH and GPG keys → New SSH key). After that you can use the SSH clone URL above.

On a restricted/shared device (e.g. a school computer) where you cannot add SSH keys, use the HTTPS clone and authenticate with your GitHub username and personal access token when prompted.

---

## Useful Git commands (cheat sheet)

This is a compact list of commands you will use frequently.

### File and status

```bash
ls                       # list files in current directory
pwd                      # print working directory
git status               # show changed files and branch
git diff                 # show unstaged changes
git add <file>           # stage a file
git add .                # stage all changes
```

### Committing

```bash
git commit -m "Short, descriptive message"   # commit staged changes
git commit --amend      # amend last commit (use with care)
```

### Branching and switching

```bash
git branch              # list branches
git branch <name>       # create a new branch
git switch <name>       # switch to <name>
git switch -c <name>    # create and switch (shortcut)
```

### Updating from remote and pushing

```bash
git fetch               # fetch updates from remote (no merge)
git pull                # fetch and merge from remote
git push origin <name>  # push branch to remote
```
When making multiple changes plese stage them individually by using `git add <file>` then `git commit -m "description"`. This can be done for all individual files changed and at the end you can run `git push origin <branch name>`.

---

## Python style & syntax rules

Follow these rules to make the codebase consistent and readable.

* **Meaningful names:** use `snake_case` for variables and functions (`player_health`, `calculate_damage`), and `PascalCase` for classes (`Player`, `Dungeon`). Choose clear, descriptive names - prefer `player_score` to `ps`.

* **Functions should do one thing:** keep functions short and focused.

* **Docstrings:** every module, function, class and method should have a docstring explaining what it does, its arguments and return values. Use triple quotes (`"""`) and follow the project's docstring style.

* **Type hints:** add type annotations for function signatures when practical to improve clarity and enable better tooling (e.g. `def move_player(x: int, y: int) -> None:`).

* **Spacing:** use blank lines to separate top-level functions and classes (two blank lines), and one blank line between methods inside classes.

* **Imports:** group imports in the order: standard library, third-party, local imports. Use absolute imports where possible.

  ```python
  import os
  import sys

  import pygame

  from .player import Player
  ```

* **Constants:** use `UPPER_SNAKE_CASE` for constants (`MAX_HEALTH = 100`).

* **Avoid long comments:** write clear code so that detailed comments are unnecessary; use comments to explain *why* a decision was made, not *what* the code does, except for functions.

* **Keep commented-out code out of the repo:** if you need to keep an experiment, use a branch or stash - don't leave commented code in `main`.

Ignore for now, I added this for the future.

* **Testing and logging:** add unit tests for game-critical logic and use logging for debug output rather than `print()` (use Python's `logging` module).

---

## Helpful tips and etiquette

* **Commit messages:** write short, descriptive messages (imperative), e.g. `Add player movement` or `Fix enemy spawn bug`.
* **Small PRs:** keep pull requests small and focused so they're easy to review.
* **Respect reviews:** address requested changes promptly and respond politely.
* **Keep `main` deployable:** avoid pushing unfinished features to `main` - use feature branches.
* **Sensitive data:** never commit passwords, tokens, or private keys. Add a `.gitignore` including typical patterns (e.g. `__pycache__/`, `.env`, `.DS_Store`).

Example `.gitignore` basics:

```
__pycache__/
*.py[cod]
.env
.vscode/
.DS_Store
```

---

---

ChatGPT was used to write **Setting up Git & GitHub** and corrected my spelling mistakes.
ChatGPT was also used to format a lot of text, mainly for:

````markdown
```bash
text in here
```
````

Everything else was writen and formated by me.


*Document created and writen by Aleksander Pietras*

*Date 28/10/2025*