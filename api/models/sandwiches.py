from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Sandwich(Base):
    __tablename__ = "sandwiches"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_name = Column(String(100), unique=True, nullable=True)
    price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')
    calories = Column(DECIMAL(4,2), nullable=False, server_default='0.0')
    ingredients = Column(String(100), unique=True, nullable=True)

    recipes = relationship("Recipe", back_populates="sandwich")
    order_details = relationship("OrderDetail", back_populates="sandwich")
    resources = relationship("Resources", back_populates="sandwich")
    promotions = relationship("Promotions", back_populates="sandwich")
    reviews = relationship("Reviews", back_populates="sandwich")
