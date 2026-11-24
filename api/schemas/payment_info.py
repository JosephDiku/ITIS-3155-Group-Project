from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PaymentBase(BaseModel):
    card_info: str
    transaction_status: str
    payment_typr: str

class PaymentCreate(PaymentBase):
    pass

class Paymentgit Update(PaymentBase):
    card_info: Optional[str] = None
    transaction_status: Optional[str] = None
    payment_typr: Optional[str] = None

class Payment(PaymentBase):
    id: int

    class ConfigDict:
        from_attributes = True