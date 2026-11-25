from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, func
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))

    # Foreign Key(s)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)
    payment_info_id = Column(Integer, ForeignKey("payment_info.id"), nullable=False)
    promo_id = Column(Integer, ForeignKey("promotions.id"), nullable=True)


    order_date = Column(DATETIME, nullable=False, server_default=func.now())
    order_status = Column(String(100))
    order_tracking = Column(Integer)
    description = Column(String(300))

    # Relationship(s)
    customer = relationship("Customer", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order")
    payment_info = relationship("PaymentInfo", back_populates="orders")
    promotion = relationship("Promotion", back_populates="orders")