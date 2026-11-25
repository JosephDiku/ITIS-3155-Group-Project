from typing import Optional
from pydantic import BaseModel



class CustomerBase(BaseModel):
    customer_name: Optional[str] = None
    customer_email: str
    customer_phone: Optional[str] = None
    customer_address: Optional[str] = None


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    customer_name: Optional[str] = None
    customer_email: Optional[str] = None
    customer_phone: Optional[str] = None
    customer_address: Optional[str] = None


class Customer(CustomerBase):
    id: int
    role: Optional[str] = None

    class ConfigDict:
        from_attributes = True