from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class PaymentInfo(Base):
    __tablename__ = "payment_info"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # Foreign Key(s)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)

    card_last4 = Column(String(4))
    transaction_status = Column(String(100))
    payment_type = Column(String(100))

    # Relationship(s)
    customer = relationship("Customer", back_populates="payments")
    orders = relationship("Order", back_populates="payment_info")
