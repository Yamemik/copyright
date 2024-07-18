from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, DateTime, String, Uuid
from sqlalchemy.orm import relationship

from ..common.database import Base, User


class Advance(Base):
    __tablename__ = "advance"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    user_id = Column(Uuid, ForeignKey(User.id), unique=True)

    # user = relationship("User", back_populates="advance")
