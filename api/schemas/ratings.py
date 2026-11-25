from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class RatingsBase(BaseModel):
    review_text: str
    score: int

class RatingsCreate(RatingsBase):
    pass

class RatingsUpdate(RatingsBase):
    review_text: Optional[str] = None
    score: Optional[int] = None

class Ratings(RatingsBase):
    id: int

    class ConfigDict:
        from_attributes = True