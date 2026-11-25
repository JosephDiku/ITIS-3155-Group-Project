from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PromotionBase(BaseModel):
    promo_code: str
    expiration_date: str
    discount: float

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(PromotionBase):
    promo_code: Optional[str] = None
    expiration_date: Optional[str] = None
    discount: Optional[float] = None

class Promotion(PromotionBase):
    id: int

    class ConfigDict:
        from_attributes = True