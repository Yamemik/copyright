from sqlalchemy import select, ScalarResult
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.feedback_model import Feedback
from ..schemas.feedback_schema import CreateUpdateFeedbackSchema


async def get_feedback_by_id(db: AsyncSession, feedback_id: int) -> Feedback | None:
    statement = select(Feedback).where(Feedback.id == feedback_id)
    selected_feedback = await db.execute(statement)
    return selected_feedback.scalars().first()


async def get_feedbacks(db: AsyncSession, skip: int = 0, limit: int = 10) -> ScalarResult | None:
    limit = limit if limit > 10 else 10
    statement = select(Feedback).offset(skip).limit(limit)
    selected_feedbacks = await db.execute(statement)
    return selected_feedbacks.scalars()


async def create_feedback(db: AsyncSession, schema: CreateUpdateFeedbackSchema):
    db_feedback = Feedback(text=schema.text, rate=schema.rate, user_id=schema.user_id)
    db.add(db_feedback)
    await db.commit()
    await db.refresh(db_feedback)
    return db_feedback


async def get_feedback_by_user(db: AsyncSession, value: str) -> Feedback | None:
    statement = select(Feedback).where(Feedback.user_id == value)
    selected_feedback = await db.execute(statement)
    return selected_feedback.scalars().first()
