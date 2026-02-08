#!/bin/bash

set -euo pipefail

mkdir -p "$(pwd)/github_copilot"
touch "$(pwd)/github_copilot/api-key.json"

docker run \
-e GITHUB_COPILOT_TOKEN_DIR="/app/github_copilot" \
-e GITHUB_COPILOT_API_KEY_FILE="api-key.json" \
-v "$(pwd)/github_copilot:/app/github_copilot" \
-v "$(pwd)/config.yaml:/app/config.yaml" \
-p 4000:4000 \
ghcr.io/berriai/litellm:main-stable \
--config /app/config.yaml --detailed_debug