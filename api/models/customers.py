from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    customer_email = Column(String(100), unique=True, nullable=False)
    customer_phone = Column(String(20))
    customer_address = Column(String(100))
    role = Column(String(20), server_default="customer")

    # Relationship(s)
    orders = relationship("Order", back_populates="customer")
    ratings = relationship("Rating", back_populates="customer")
    payments = relationship("PaymentInfo", back_populates="customer")
