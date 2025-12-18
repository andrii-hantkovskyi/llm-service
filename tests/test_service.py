from unittest.mock import AsyncMock, MagicMock

import pytest

from app.application.generation_service import GenerationService
from app.domain.schemas import GenerationRequest


@pytest.mark.asyncio
async def test_process_request_success() -> None:
    mock_provider = MagicMock()
    mock_provider.generate_response = AsyncMock(return_value={"result": "ok"})

    mock_factory = MagicMock()
    mock_factory.get_provider.return_value = mock_provider

    service = GenerationService(factory=mock_factory)

    request = GenerationRequest(provider="test_provider", prompt="Hello")
    response = await service.process_request(request)

    mock_factory.get_provider.assert_called_once_with("test_provider")
    mock_provider.generate_response.assert_called_once_with("Hello")
    assert response.provider == "test_provider"
    assert response.result == {"result": "ok"}
