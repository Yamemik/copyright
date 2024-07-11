from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, Float, DateTime, String
from sqlalchemy.orm import relationship

from ..common.database import Base


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    text = Column(String)
    rate = Column(Integer, default=5)
    user_id = Column(Integer, ForeignKey("user.id"), unique=True)

    user = relationship("User", back_populates="feedbacks")
