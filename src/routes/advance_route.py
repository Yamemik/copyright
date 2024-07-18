from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ..schemas import feedback_schema
from ..services import feedback_service
from ..common.database import get_async_session


course_router = APIRouter(
    prefix="/api/advances",
    tags=["Достижения пользователей"],
)


@course_router.get(
    "",
    # response_model=list[feedback_schema.FeedbackSchema],
    summary="Получить достижение",
    status_code=status.HTTP_202_ACCEPTED
)
def read_advances(skip: int = 0, limit: int = 20, ):
    pass
