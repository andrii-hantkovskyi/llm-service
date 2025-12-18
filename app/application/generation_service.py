from app.domain.schemas import GenerationRequest, GenerationResponse
from app.infrastructure.llm_registry import LLMProviderFactory


class GenerationService:
    def __init__(self, factory: LLMProviderFactory):
        self.factory = factory

    async def process_request(self, request: GenerationRequest) -> GenerationResponse:
        provider = self.factory.get_provider(request.provider)

        llm_data = await provider.generate_response(request.prompt)

        return GenerationResponse(provider=request.provider.value, result=llm_data)
