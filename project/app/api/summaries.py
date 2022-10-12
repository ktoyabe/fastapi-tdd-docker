from fastapi import APIRouter, HTTPException, status

from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema


router = APIRouter()


@router.post("/", response_model=SummaryPayloadSchema, status_code=status.HTTP_201_CREATED)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    summary_id = await crud.post(payload)

    response_object = {
        "id": summary_id,
        "url": payload.url
    }
    return response_object