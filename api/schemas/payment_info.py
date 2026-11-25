from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PaymentBase(BaseModel):
    customer_id: Optional[str] = None
    card_last4: Optional[str] = None
    transaction_status: Optional[str] = None
    payment_type: Optional[str] = None

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(PaymentBase):
    card_last4: Optional[str] = None
    transaction_status: Optional[str] = None
    payment_type: Optional[str] = None

class Payment(PaymentBase):
    id: int

    class ConfigDict:
        from_attributes = True