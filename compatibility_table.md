| model | /v1/chat/completions | /v1/messages | /v1/responses | notes |
| --- | --- | --- | --- | --- |
| gemini-2.5-pro | OK | OK | FAIL (400) | /v1/responses: litellm.BadRequestError: Github_copilotException - {"error":{"message":"model gemini-2.5-pro is not supported via Respon |
| gemini-3-flash-preview | OK | OK | FAIL (400) | /v1/responses: litellm.BadRequestError: Github_copilotException - {"error":{"message":"model gemini-3-flash-preview is not supported vi |
| gemini-3-pro-preview | OK | OK | FAIL (400) | /v1/responses: litellm.BadRequestError: Github_copilotException - {"error":{"message":"model gemini-3-pro-preview is not supported via  |
| gpt-4.1 | OK | OK | FAIL (400) | /v1/responses: litellm.BadRequestError: Github_copilotException - {"error":{"message":"model gpt-4.1 is not supported via Responses API |
| gpt-4o | OK | OK | FAIL (400) | /v1/responses: litellm.BadRequestError: Github_copilotException - {"error":{"message":"model gpt-4o is not supported via Responses API. |
| gpt-5 | OK | OK | OK |  |
| gpt-5-mini | OK | OK | OK |  |
| gpt-5-codex | FAIL (400) | FAIL (400) | OK | /v1/chat/completions: litellm.BadRequestError: Github_copilotException - model gpt-5-codex is not supported in this VS Code version. Please up | /v1/messages: litellm.BadRequestError: Github_copilotException - model gpt-5-codex is not supported in this VS Code version. Please up |
| gpt-5.1 | OK | OK | OK |  |
| gpt-5.1-codex | FAIL (400) | FAIL (400) | OK | /v1/chat/completions: litellm.BadRequestError: Github_copilotException - model gpt-5.1-codex is not accessible via the /chat/completions endpo | /v1/messages: litellm.BadRequestError: Github_copilotException - model gpt-5.1-codex is not accessible via the /chat/completions endpo |
| gpt-5.1-codex-max | OK | FAIL (500) | OK | /v1/messages: litellm.APIConnectionError: APIConnectionError: Github_copilotException - gpt-5.1-codex-max unable to complete request:  |
| gpt-5.1-codex-mini | FAIL (400) | FAIL (400) | OK | /v1/chat/completions: litellm.BadRequestError: Github_copilotException - model gpt-5.1-codex-mini is not accessible via the /chat/completions  | /v1/messages: litellm.BadRequestError: Github_copilotException - model gpt-5.1-codex-mini is not accessible via the /chat/completions  |
| gpt-5.2 | OK | OK | OK |  |
| gpt-5.2-codex | FAIL (400) | FAIL (400) | OK | /v1/chat/completions: litellm.BadRequestError: Github_copilotException - model gpt-5.2-codex is not accessible via the /chat/completions endpo | /v1/messages: litellm.BadRequestError: Github_copilotException - model gpt-5.2-codex is not accessible via the /chat/completions endpo |
| grok-code-fast-1 | OK | OK | FAIL (400) | /v1/responses: litellm.BadRequestError: Github_copilotException - {"error":{"message":"model grok-code-fast-1 is not supported via Resp |
| claude-sonnet-4.5 | OK | OK | FAIL (400) | /v1/responses: litellm.BadRequestError: Github_copilotException - {"error":{"message":"model claude-sonnet-4.5 does not support Respons |
| claude-opus-4.5 | OK | OK | FAIL (400) | /v1/responses: litellm.BadRequestError: Github_copilotException - {"error":{"message":"model claude-opus-4.5 does not support Responses |
| claude-opus-4.6 | OK | OK | FAIL (400) | /v1/responses: litellm.BadRequestError: Github_copilotException - {"error":{"message":"model claude-opus-4.6 does not support Responses |
| claude-haiku-4.5 | OK | OK | FAIL (400) | /v1/responses: litellm.BadRequestError: Github_copilotException - {"error":{"message":"model claude-haiku-4.5 does not support Response |
