class LLMServiceError(Exception):
    """Base exception for the LLM service."""

    pass


class ProviderNotFoundError(LLMServiceError):
    """Raised when a requested LLM provider is not registered."""

    def __init__(self, provider_name: str):
        self.message = f"Provider '{provider_name}' is not supported."
        super().__init__(self.message)


class ExternalAPIError(LLMServiceError):
    """Raised when the external LLM API fails (timeout, 500s, etc.)."""

    def __init__(self, provider_name: str, details: str):
        self.message = f"Error communicating with {provider_name}: {details}"
        super().__init__(self.message)
