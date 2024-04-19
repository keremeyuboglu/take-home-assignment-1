from typing import List, Optional
from pydantic import BaseModel

class GetMenuItemsResponse(BaseModel):
    name: str
    description: Optional[str]
    stock_status: str
    image: Optional[str]
    ranking: Optional[int]
    price: float
    calorie: Optional[float]
    
class GetMenuGroupResponse(BaseModel):
    name: str
    sort_order: int
    menu_items: List[GetMenuItemsResponse]  

class GetMenuResponse(BaseModel):
    menu_groups: List[GetMenuGroupResponse]
    
    
class MenuItemUpdateRequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    stock_status: Optional[str] = None
    image: Optional[str] = None
    ranking: Optional[int] = None
    price: Optional[float] = None
    calorie: Optional[float] = None

class PostMenuRequest(BaseModel):
    type: str
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    stock_status: Optional[str] = None
    image: Optional[str] = None
    ranking: Optional[int] = None
    price: Optional[float] = None
    calorie: Optional[float] = None
    
        
class InsertMenuRequest(BaseModel):
    name: str 
    description: Optional[str] = None
    stock_status: Optional[str] = None
    image: Optional[str] = None
    price: Optional[float] = None
    calorie: Optional[float] = None
    
class UpdateMenuRequest(BaseModel):
    id: int 
    name: Optional[str] = None
    description: Optional[str] = None
    stock_status: Optional[str] = None
    image: Optional[str] = None
    ranking: Optional[int] = None
    price: Optional[float] = None
    calorie: Optional[float] = None
    
class DeleteMenuRequest(BaseModel):
    id: int