from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class RatingsBase(BaseModel):
    review_text: Optional[str] = None
    score: int

class RatingsCreate(RatingsBase):
    pass

class RatingsUpdate(RatingsBase):
    review_text: Optional[str] = None
    score: Optional[int] = None

class Ratings(RatingsBase):
    id: int
    customer_id: int
    sandwich_id: int

    class ConfigDict:
        from_attributes = True