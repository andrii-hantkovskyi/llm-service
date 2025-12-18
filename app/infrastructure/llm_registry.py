from typing import Dict

from app.domain.exceptions import ProviderNotFoundError
from app.domain.interfaces import ILLMProvider


class LLMProviderFactory:
    def __init__(self) -> None:
        self._providers: Dict[str, ILLMProvider] = {}

    def register_provider(self, key: str, provider: ILLMProvider) -> None:
        self._providers[key] = provider

    def get_provider(self, key: str) -> ILLMProvider:
        provider = self._providers.get(key)
        if not provider:
            raise ProviderNotFoundError(key)
        return provider
