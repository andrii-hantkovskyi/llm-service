from fastapi import APIRouter, Depends, HTTPException

from app.application.generation_service import GenerationService
from app.dependencies import get_service
from app.domain.exceptions import ExternalAPIError, ProviderNotFoundError
from app.domain.schemas import GenerationRequest, GenerationResponse

router = APIRouter()


@router.post("/generate", response_model=GenerationResponse)
async def generate_text(
    request: GenerationRequest, service: GenerationService = Depends(get_service)
) -> GenerationResponse:
    try:
        return await service.process_request(request)
    except ProviderNotFoundError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    except ExternalAPIError as e:
        raise HTTPException(status_code=502, detail=str(e)) from e
    except Exception:
        # Log the actual error internally here
        raise HTTPException(status_code=500, detail="Internal Service Error") from None
