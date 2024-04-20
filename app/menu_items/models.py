from typing import Optional
from pydantic import BaseModel

class MenuItemUpdateRequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    stock_status: Optional[str] = None
    image: Optional[str] = None
    ranking: Optional[int] = None
    price: Optional[float] = None
    calorie: Optional[float] = None