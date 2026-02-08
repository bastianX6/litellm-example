# AGENTS

This repository is a small, local LiteLLM proxy setup for GitHub Copilot.

## Responsibilities

- Keep `run-docker.sh` focused on starting the proxy and managing persistence.
- Keep `config.yaml` as the single source of truth for models and headers.
- Use `compatibility_check.py` to verify endpoint compatibility and regenerate `compatibility_table.md`.
- Avoid adding unrelated tooling or frameworks.

## Conventions

- Use relative paths within scripts.
- Keep changes minimal and explicit.
- Prefer plain Markdown documentation.

## Safety

- Do not commit token files or secrets.
- Keep the `.gitignore` updated for any local auth artifacts.
