from typing import Optional
from decimal import Decimal
from pydantic import BaseModel


class SandwichBase(BaseModel):
    sandwich_name: Optional[str] = None
    price: Decimal
    ingredients: Optional[str] = None
    calories: int


class SandwichCreate(SandwichBase):
    pass


class SandwichUpdate(BaseModel):
    sandwich_name: Optional[str] = None
    price: Optional[Decimal] = None
    ingredients: Optional[str] = None
    calories: Optional[int] = None


class Sandwich(SandwichBase):
    id: int

    class ConfigDict:
        from_attributes = True