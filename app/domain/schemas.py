from typing import Any

from pydantic import BaseModel, Field


class GenerationRequest(BaseModel):
    provider: str = Field(..., description="The name of the LLM provider (e.g., 'openai', 'mock')")
    prompt: str = Field(..., description="The input text for the model")


class GenerationResponse(BaseModel):
    provider: str
    result: dict[str, Any]
