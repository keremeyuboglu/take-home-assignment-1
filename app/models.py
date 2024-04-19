from typing import List, Optional
from pydantic import BaseModel

class MenuItemsResponse(BaseModel):
    name: str
    description: Optional[str]
    stock_status: str
    image: Optional[str]
    ranking: Optional[int]
    price: float
    calorie: Optional[float]
    
class MenuGroupResponse(BaseModel):
    name: str
    sort_order: int
    menu_items: List[MenuItemsResponse]  

class MenuResponse(BaseModel):
    menu_groups: List[MenuGroupResponse]
    
class MenuItemUpdateRequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    stock_status: Optional[str] = None
    image: Optional[str] = None
    ranking: Optional[int] = None
    price: Optional[float] = None
    calorie: Optional[float] = None

class RequestBodyModel(BaseModel):
    type: str
    id: int
    name: Optional[str] = None
    description: Optional[str] = None
    stock_status: Optional[str] = None
    image: Optional[str] = None
    ranking: Optional[int] = None
    price: Optional[float] = None
    calorie: Optional[float] = None