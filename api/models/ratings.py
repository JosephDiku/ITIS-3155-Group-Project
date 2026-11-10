from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    review_text = Column(String(100))
    score = Column(DECIMAL(10,2))
