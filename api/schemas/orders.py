from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail, OrderDetailCreate



class OrderBase(BaseModel):
    customer_name: str
    customer_id: Optional[int] = None
    description: Optional[str] = None
    payment_info_id: Optional[int] = None
    promo_id: Optional[int] = None
    order_status: Optional[str] = None
    order_tracking: Optional[int] = None
    


class OrderCreate(BaseModel):
    customer_id: int
    description: Optional[str] = None
    payment_info_id: Optional[int] = None
    promo_id: Optional[int] = None
    order_details: list[OrderDetailCreate]


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    customer_id: Optional[int] = None
    description: Optional[str] = None
    payment_info_id: Optional[int] = None
    promo_id: Optional[int] = None
    order_status: Optional[str] = None
    order_tracking: Optional[int] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    payment_info_id: Optional[int] = None
    promo_id: Optional[int] = None
    order_status: Optional[str] = None
    order_tracking: Optional[int] = None
    order_details: list[OrderDetail] = []

    class ConfigDict:
        from_attributes = True
