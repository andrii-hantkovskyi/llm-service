import asyncio
from typing import Any, Dict

from app.domain.interfaces import ILLMProvider


class MockProvider(ILLMProvider):
    """
    A fake provider for testing and development.
    Does not make external network calls.
    """

    async def generate_response(self, prompt: str) -> Dict[str, Any]:
        await asyncio.sleep(0.5)

        return {
            "status": "success",
            "model": "mock-gpt-v1",
            "reply": f"This is a mocked response to your prompt: '{prompt}'",
            "data": {"usage": 15, "confidence": 0.99},
        }
