from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ..schemas import feedback_schema
from ..services import feedback_service
from ..models import feedback_model
from ..common.database import get_async_session, engine


# feedback_model.Base.metadata.create_all(bind=engine)


feedback_router = APIRouter(
    prefix="/api/feedbacks",
    tags=["Отзывы пользователей"],
)


def get_db():
    db = get_async_session()
    try:
        yield db
    finally:
        db.aclose()


@feedback_router.get(
    "",
    response_model=list[feedback_schema.FeedbackSchema],
    summary="Получить отзывы",
    status_code=status.HTTP_202_ACCEPTED
)
def read_feedbacks(skip: int = 0, limit: int = 20, db: AsyncSession = Depends(get_db)):
    selected_feedbacks = feedback_service.get_feedbacks(db, skip=skip, limit=limit)
    return selected_feedbacks


@feedback_router.get(
    "/{feedback_id}",
    response_model=feedback_schema.FeedbackSchema,
    summary="Получить отзыв по id",
)
def read_feedback(feedback_id: int, db: AsyncSession = Depends(get_db)):
    selected_feedback = feedback_service.get_feedback_by_id(db, feedback_id=feedback_id)
    if selected_feedback is None:
        raise HTTPException(status_code=404, detail="Feedback not found")
    else:
        return selected_feedback


@feedback_router.get(
    "/user/{user_id}",
    response_model=feedback_schema.FeedbackSchema,
    summary="Получить отзыв по пользователю",
)
def read_feedback_by_user(user_id: str, db: AsyncSession = Depends(get_db)):
    selected_feedback = feedback_service.get_feedback_by_user(db, value=user_id)
    print(selected_feedback)
    if selected_feedback is None:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return selected_feedback


@feedback_router.post(
    "",
    response_model=feedback_schema.FeedbackSchema,
    summary="Создать отзыв",
    status_code=status.HTTP_201_CREATED,
)
def write_feedback(create_schema: feedback_schema.CreateUpdateFeedbackSchema, db: AsyncSession = Depends(get_db)):
    db_role = feedback_service.create_feedback(db, schema=create_schema)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not create")
    return db_role
