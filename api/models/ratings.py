from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # Foreign Key(s)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"), nullable=False)

    review_text = Column(String(100))
    score = Column(Integer)

    # Relationship(s)
    customer = relationship("Customer", back_populates="ratings")
    sandwich = relationship("Sandwich", back_populates="ratings")
