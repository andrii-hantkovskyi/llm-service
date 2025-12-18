from typing import Dict

from app.domain.exceptions import ProviderNotFoundError
from app.domain.interfaces import ILLMProvider
from app.domain.schemas import ProviderType


class LLMProviderFactory:
    def __init__(self) -> None:
        self._providers: Dict[ProviderType, ILLMProvider] = {}

    def register_provider(self, key: ProviderType, provider: ILLMProvider) -> None:
        self._providers[key] = provider

    def get_provider(self, key: ProviderType) -> ILLMProvider:
        provider = self._providers.get(key)
        if not provider:
            raise ProviderNotFoundError(key.value)
        return provider
