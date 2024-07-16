from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ..schemas import feedback_schema
from ..services import feedback_service
from ..common.database import get_async_session


course_router = APIRouter(
    prefix="/api/courses",
    tags=["Курсы пользователей"],
)


@course_router.get(
    "",
    # response_model=list[feedback_schema.FeedbackSchema],
    summary="Получить курсы",
    status_code=status.HTTP_202_ACCEPTED
)
def read_courses(skip: int = 0, limit: int = 20, ):
    pass
