from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.dependencies import setup_providers
from app.presentation.router import router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    setup_providers()
    yield


app = FastAPI(title="LLM Manager Service", lifespan=lifespan)

app.include_router(router)
