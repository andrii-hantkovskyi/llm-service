from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class ProviderType(Enum):
    OPENAI = "openai"
    MOCK = "mock"


class GenerationRequest(BaseModel):
    provider: ProviderType = Field(..., description="The name of the LLM provider (e.g., 'openai', 'mock')")
    prompt: str = Field(..., description="The input text for the model")


class GenerationResponse(BaseModel):
    provider: str
    result: dict[str, Any]
