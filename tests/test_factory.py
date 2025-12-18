import pytest

from app.domain.exceptions import ProviderNotFoundError
from app.domain.interfaces import ILLMProvider
from app.infrastructure.llm_registry import LLMProviderFactory


class DummyProvider(ILLMProvider):
    async def generate_response(self, prompt: str) -> dict[str, str]:
        return {}


def test_factory_register_and_retrieve() -> None:
    factory = LLMProviderFactory()
    provider = DummyProvider()

    factory.register_provider("dummy", provider)

    retrieved = factory.get_provider("dummy")
    assert retrieved is provider


def test_factory_raises_error_for_unknown_provider() -> None:
    factory = LLMProviderFactory()

    with pytest.raises(ProviderNotFoundError) as excinfo:
        factory.get_provider("ghost_provider")

    assert "not supported" in str(excinfo.value)
