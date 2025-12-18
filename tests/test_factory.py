from unittest.mock import MagicMock

import pytest

from app.domain.exceptions import ProviderNotFoundError
from app.domain.interfaces import ILLMProvider
from app.domain.schemas import ProviderType
from app.infrastructure.llm_registry import LLMProviderFactory


class DummyProvider(ILLMProvider):
    async def generate_response(self, prompt: str) -> dict[str, str]:
        return {}


def test_factory_works() -> None:
    factory = LLMProviderFactory()
    mock_provider = MagicMock()

    factory.register_provider(ProviderType.MOCK, mock_provider)
    assert factory.get_provider(ProviderType.MOCK) == mock_provider


def test_factory_raises_error_for_unknown_provider() -> None:
    factory = LLMProviderFactory()

    with pytest.raises(ProviderNotFoundError):
        factory.get_provider(ProviderType.OPENAI)
