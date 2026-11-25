from sqlalchemy import Column, ForeignKey, Integer, String, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = 'promotions'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promo_code = Column(String(5), unique=True, nullable=False)
    expiration_date = Column(String(10))
    discount = Column(DECIMAL(2,2))

    # Relationship(s)
    orders = relationship("Order", back_populates="promotion")