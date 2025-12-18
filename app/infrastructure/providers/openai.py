import json
from typing import Any, cast

import httpx

from app.domain.exceptions import ExternalAPIError
from app.domain.interfaces import ILLMProvider


class OpenAIProvider(ILLMProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.url = "https://api.openai.com/v1/responses"

    async def generate_response(self, prompt: str) -> dict[str, Any]:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    self.url,
                    headers={"Authorization": f"Bearer {self.api_key}"},
                    json={
                        "model": "gpt-4o",
                        "input": [{"type": "text", "text": prompt}],
                        "text": {
                            "json_schema": {
                                "name": "response_schema",
                                "strict": True,
                                "schema": {
                                    "type": "object",
                                    "properties": {"reply": {"type": "string"}, "metadata": {"type": "string"}},
                                    "required": ["reply", "metadata"],
                                    "additionalProperties": False,
                                },
                            }
                        },
                    },
                    timeout=30.0,
                )
                response.raise_for_status()

                data = response.json()

                raw_content = data.get("output_text")

                # Fallback if the API returns it nested (common in transition phases)
                if not raw_content and "message" in data:
                    raw_content = data["message"].get("output_text")

                if not raw_content:
                    raise ValueError("API response is missing expected 'output_text'")

                return cast(dict[str, Any], json.loads(raw_content))

            except httpx.HTTPStatusError as e:
                raise ExternalAPIError("openai", f"HTTP {e.response.status_code}: {e.response.text}") from e
            except (json.JSONDecodeError, ValueError) as e:
                raise ExternalAPIError("openai", f"Failed to parse response: {str(e)}") from e
