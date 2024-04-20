from app.entities import MenuItem, db
from sqlalchemy import update
from app.menu_items.models import MenuItemUpdateRequest


def update_menu_item(menu_item_id: int, body: MenuItemUpdateRequest) -> None:
    stmt = (
        update(MenuItem)
        .where(MenuItem.id == menu_item_id)
        .values(
            body.model_dump(
                exclude_none=True,
                exclude="id"
                )
            )
        )
    db.session.execute(stmt)
    db.session.commit()
