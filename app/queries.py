from .entities import Menu, MenuGroup, MenuGroupItemMap, Restaurant, MenuItem, db
from sqlalchemy import delete, update, insert
from .models import *

def get_menu_by_restaurant_id(restaurant_id: int) -> Menu:
    menu: Menu = db.session.scalars(
            db.select(Menu).filter_by(restaurant_id=restaurant_id).order_by(Menu.created_at.desc()).limit(1)
            ).first()  
    return menu   

def delete_menu_item(restaurant_id: int, body: RequestBodyModel) -> None:
    stmt = delete(MenuItem).where(MenuItem.id == body.id, MenuItem.restaurant_id == restaurant_id)
    db.session.execute(stmt)
    db.session.commit()
    
def update_menu_items(restaurant_id: int, body: RequestBodyModel) -> None:
    stmt = update(MenuItem).where(MenuItem.id == body.id, MenuItem.restaurant_id == restaurant_id).values(
            body.model_dump(exclude={'type', 'id'}, exclude_none=True)
        )
    db.session.execute(stmt)
    db.session.commit()
    
    
def insert_menu_item(restaurant_id: int, body: RequestBodyModel) -> None:
    stmt = insert(MenuItem).values(
        body.model_dump(exclude={'type', 'id'}),
        restaurant_id=restaurant_id
    )
    db.session.execute(stmt)
    db.session.commit()
    
def update_menu_item(menu_item_id: int, body: RequestBodyModel) -> None:
    stmt = update(MenuItem).where(MenuItem.id == menu_item_id).values(
        body.model_dump(exclude_none=True)
    )
    db.session.execute(stmt)
    db.session.commit()