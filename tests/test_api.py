import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_generate_with_mock_provider(client: AsyncClient) -> None:
    payload = {"provider": "mock", "prompt": "Hello, world!"}

    response = await client.post("/generate", json=payload)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_provider_not_found(client: AsyncClient) -> None:
    payload = {"provider": "non-existent-ai", "prompt": "This should fail"}

    response = await client.post("/generate", json=payload)

    assert response.status_code == 400
