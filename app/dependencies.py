from app.application.generation_service import GenerationService
from app.infrastructure.config import settings
from app.infrastructure.llm_registry import LLMProviderFactory
from app.infrastructure.providers.mock import MockProvider
from app.infrastructure.providers.openai import OpenAIProvider

PROVIDER_MAP = {
    "openai": (OpenAIProvider, "OPENAI_API_KEY"),
    # Future providers (e.g., Anthropic, Mistral) are just one line:
    # "mistral": (MistralProvider, "MISTRAL_API_KEY"),
}

llm_factory = LLMProviderFactory()


def setup_providers() -> None:
    """Dynamically registers providers based on available config."""
    # Always register the mock provider
    llm_factory.register_provider("mock", MockProvider())

    for name, (provider_cls, setting_key) in PROVIDER_MAP.items():
        api_key = getattr(settings, setting_key, None)

        if api_key:
            llm_factory.register_provider(name, provider_cls(api_key))


def get_service() -> GenerationService:
    return GenerationService(llm_factory)
