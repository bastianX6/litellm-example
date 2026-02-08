import json
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE_URL = "http://localhost:4000"
API_KEY = "your-proxy-api-key"
BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "config.yaml"
OUT_PATH = BASE_DIR / "compatibility_table.md"
DELAY_SECONDS = 5

models = []
skip_block = False
for line in CONFIG_PATH.read_text().splitlines():
    stripped = line.strip()
    if stripped == "# Claude code models":
        skip_block = True
        continue
    if stripped == "# End of Claude code models":
        skip_block = False
        continue
    if skip_block:
        continue
    if stripped.startswith("- model_name:"):
        models.append(stripped.split(":", 1)[1].strip())

endpoints = [
    ("/v1/chat/completions", "chat"),
    ("/v1/messages", "messages"),
    ("/v1/responses", "responses"),
]


def request_payload(model: str, kind: str) -> dict:
    if kind == "chat":
        return {"model": model, "messages": [{"role": "user", "content": "Compat test."}]}
    if kind == "messages":
        return {"model": model, "max_tokens": 32, "messages": [{"role": "user", "content": "Compat test."}]}
    if kind == "responses":
        return {"model": model, "input": "Compat test."}
    raise ValueError(kind)


results: dict[str, dict[str, tuple[object, str]]] = {m: {} for m in models}

for model in models:
    for endpoint, kind in endpoints:
        url = f"{BASE_URL}{endpoint}"
        payload = request_payload(model, kind)
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}",
            },
            method="POST",
        )
        status: object
        note = ""
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                status = resp.getcode()
                body = resp.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            status = exc.code
            body = exc.read().decode("utf-8")
        except Exception as exc:  # noqa: BLE001
            status = "ERR"
            note = str(exc)
            results[model][endpoint] = (status, note)
            time.sleep(DELAY_SECONDS)
            continue

        if isinstance(status, int) and 200 <= status < 300:
            results[model][endpoint] = (status, "OK")
            time.sleep(DELAY_SECONDS)
            continue

        msg = ""
        try:
            payload = json.loads(body)
            if isinstance(payload, dict):
                msg = payload.get("error", {}).get("message") or payload.get("error") or ""
        except Exception:  # noqa: BLE001
            msg = ""
        if not msg:
            msg = body.strip().splitlines()[0] if body else ""
        msg = msg[:120]
        results[model][endpoint] = (status, msg or "FAIL")

        time.sleep(DELAY_SECONDS)

lines = [
    "| model | /v1/chat/completions | /v1/messages | /v1/responses | notes |",
    "| --- | --- | --- | --- | --- |",
]

for model in models:
    row = [model]
    notes = []
    for endpoint, _kind in endpoints:
        status, msg = results[model].get(endpoint, ("ERR", ""))
        if status == "ERR":
            cell = "ERR"
        elif isinstance(status, int) and 200 <= status < 300:
            cell = "OK"
        else:
            cell = f"FAIL ({status})"
            if msg and msg != "FAIL":
                notes.append(f"{endpoint}: {msg}")
        row.append(cell)
    note_text = " | ".join(notes) if notes else ""
    row.append(note_text)
    lines.append("| " + " | ".join(row) + " |")

OUT_PATH.write_text("\n".join(lines) + "\n")
print(f"Wrote {OUT_PATH}")
