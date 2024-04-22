from app.entities import MenuItem, db
from sqlalchemy import update
from app.menu_items.models import MenuItemUpdateRequestSchema
from sqlalchemy.exc import IntegrityError


def update_menu_item(menu_item_id: int, body: MenuItemUpdateRequestSchema) -> None:
    stmt = (
        update(MenuItem)
        .where(MenuItem.id == menu_item_id)
        .values(body).returning(MenuItem)
    )
    try:
        menu_item = db.session.scalar(stmt)
        return menu_item
    except Exception as e:
        raise e
    
