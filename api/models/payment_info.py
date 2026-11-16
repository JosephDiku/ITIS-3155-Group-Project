from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Payment(Base):
    __tablename__ = "payment_info"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    card_info = Column(String(100), primary_key=True)
    transaction_status = Column(String(100))
    payment_type = Column(String(100))

