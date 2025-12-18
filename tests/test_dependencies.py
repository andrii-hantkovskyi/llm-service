from unittest.mock import MagicMock, patch

from app.dependencies import llm_factory, setup_providers
from app.infrastructure.providers.openai import OpenAIProvider


def test_setup_providers_registers_mock() -> None:
    """Test that 'mock' provider is always registered."""
    llm_factory._providers = {}

    setup_providers()

    assert "mock" in llm_factory._providers


@patch("app.dependencies.settings")
def test_setup_providers_registers_openai_when_key_exists(mock_settings: MagicMock) -> None:
    """Test that OpenAI is registered when API Key is present in settings."""
    mock_settings.OPENAI_API_KEY = "sk-test-key-123"

    llm_factory._providers = {}
    setup_providers()

    assert "openai" in llm_factory._providers
    provider = llm_factory.get_provider("openai")
    assert isinstance(provider, OpenAIProvider)
    assert provider.api_key == "sk-test-key-123"


@patch("app.dependencies.settings")
def test_setup_providers_skips_openai_when_no_key(mock_settings: MagicMock) -> None:
    """Test that OpenAI is NOT registered when API Key is missing."""
    mock_settings.OPENAI_API_KEY = None

    llm_factory._providers = {}
    setup_providers()

    assert "openai" not in llm_factory._providers
