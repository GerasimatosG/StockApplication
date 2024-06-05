from pydantic import BaseModel
from typing import Optional

class ItemBaseModel(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    availability: Optional[int] = None