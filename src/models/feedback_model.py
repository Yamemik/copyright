from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, DateTime, String, Uuid
from sqlalchemy.orm import relationship

from ..common.database import Base, User


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    text = Column(String)
    rate = Column(Integer, default=5)
    user_id = Column(Uuid, ForeignKey(User.id))

    user = relationship("User", back_populates="feedbacks")

