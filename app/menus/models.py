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

class PostMenuRequest(BaseModel):
    type: str
    menu_item_id: int
        
class InsertMenuItemToMenuRequest(BaseModel):
    menu_item_id: int

class DeleteMenuItemFromMenuRequest(BaseModel):
    menu_item_id: int