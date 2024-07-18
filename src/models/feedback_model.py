from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, DateTime, String, Uuid
from sqlalchemy.orm import relationship
from sqladmin import ModelView

from ..common.database import Base, User


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    text = Column(String)
    rate = Column(Integer, default=5)
    user_id = Column(Uuid, ForeignKey(User.id))

    user = relationship("User", back_populates="feedbacks")


class FeedbackAdmin(ModelView, model=Feedback):
    name = "Отзыв"
    name_plural = "Отзывы"
    icon = "fa-sharp fa-solid fa-credit-card-alt"
    column_list = "__all__"
