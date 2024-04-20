from app.entities import Menu, MenuItem, MenuGroup, db
from sqlalchemy import update, insert, desc, and_, orm
from app.menus.models import *

def get_menu_by_restaurant_id(restaurant_id: int) -> Menu:
    stmt = db.select(Menu).where(Menu.restaurant_id == restaurant_id).options(
        orm.selectinload(Menu.menu_groups).selectinload(
            MenuGroup.menu_items.and_(MenuItem.is_deleted==False)
        )
    )
    menu: Menu = db.session.scalars(stmt).first()  
    return menu   

def delete_menu_item_from_menu(restaurant_id:int, menu_item_id: int) -> None:
    stmt = update(MenuItem).where(MenuItem.id==menu_item_id,
                                  MenuItem.restaurant_id==restaurant_id
                                  ).values(is_deleted=True)
    db.session.execute(stmt)
    db.session.commit()
    
    
def insert_menu_item_to_menu(restaurant_id:int, menu_item_id: int) -> None:
    stmt = update(MenuItem).where(MenuItem.id==menu_item_id,
                                  MenuItem.restaurant_id==restaurant_id
                                  ).values(is_deleted=False)
    db.session.execute(stmt)
    db.session.commit()
    