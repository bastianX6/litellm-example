# LiteLLM GitHub Copilot Proxy

This repository contains a minimal LiteLLM proxy setup for routing requests to GitHub Copilot models.

## What it does

- Runs the LiteLLM proxy in Docker.
- Loads model configuration from `config.yaml`.
- Persists GitHub Copilot token data on the host.
- Provides a compatibility test script for proxy endpoints.

## Key files

- `run-docker.sh`: Starts the LiteLLM proxy container with the required mounts and env vars.
- `config.yaml`: Model and header configuration used by the proxy.
- `compatibility_check.py`: Runs sequential endpoint tests and writes `compatibility_table.md`.
- `compatibility_table.md`: Generated compatibility matrix for the configured models.

## Quick start

1. Start the proxy:

   ```bash
   sh run-docker.sh
   ```

2. Run compatibility checks:

   ```bash
   python3 compatibility_check.py
   ```

## Configuration notes

- GitHub Copilot headers are defined once and reused across models via YAML anchors.
- The proxy listens on `http://localhost:4000` by default.
- Token files are stored under the host directory mounted by `run-docker.sh`.

## Repository scope

This is a lightweight, local setup intended for development and testing of the proxy configuration and model compatibility.
