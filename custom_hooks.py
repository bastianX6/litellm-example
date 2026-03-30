import json
from litellm.integrations.custom_logger import CustomLogger

print("[FixArraySchemas] >>> custom_hooks.py imported", flush=True)


class FixArraySchemas(CustomLogger):
    """Pre-call hook that patches array-type properties missing the required
    'items' field in tool/function JSON Schemas.

    Claude/Anthropic accepts schemas without 'items', but GPT-based models
    (OpenAI, GitHub Copilot) enforce strict JSON Schema validation and return
    a 400 error when 'items' is absent. This hook normalises the schema before
    it reaches the provider.
    """

    def _fix_schema(self, props: dict) -> int:
        """Recursively patch arrays missing 'items'. Returns count of patches applied."""
        patches = 0
        for v in props.values():
            if not isinstance(v, dict):
                continue
            if v.get("type") == "array" and "items" not in v:
                v["items"] = {}
                patches += 1
                print(f"[FixArraySchemas] Patched array missing 'items': {v}", flush=True)
            if "properties" in v:
                patches += self._fix_schema(v["properties"])
            if "items" in v and isinstance(v["items"], dict) and "properties" in v["items"]:
                patches += self._fix_schema(v["items"]["properties"])
        return patches

    async def async_pre_call_hook(self, user_api_key_dict, cache, data, call_type):
        tools = data.get("tools") or []
        print(
            f"[FixArraySchemas] >>> async_pre_call_hook fired "
            f"call_type={call_type} tools_count={len(tools)} "
            f"data_keys={list(data.keys())}",
            flush=True,
        )
        total_patches = 0
        for tool in tools:
            props = (
                tool.get("function", {})
                    .get("parameters", {})
                    .get("properties", {})
            )
            total_patches += self._fix_schema(props)

        print(f"[FixArraySchemas] >>> hook done — total patches applied: {total_patches}", flush=True)
        return data

    def log_pre_api_call(self, model, messages, kwargs):
        """Backup interception point: called by litellm core just before the API call.
        Modifies kwargs['tools'] in-place as a second line of defence."""
        tools = kwargs.get("tools") or []
        print(
            f"[FixArraySchemas] >>> log_pre_api_call fired model={model} tools_count={len(tools)}",
            flush=True,
        )
        for tool in tools:
            props = (
                tool.get("function", {})
                    .get("parameters", {})
                    .get("properties", {})
            )
            self._fix_schema(props)


proxy_handler_instance = FixArraySchemas()
print(f"[FixArraySchemas] >>> proxy_handler_instance created: {proxy_handler_instance}", flush=True)
