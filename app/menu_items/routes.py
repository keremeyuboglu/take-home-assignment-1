from flask import Blueprint
from flask_pydantic import validate
from app.menu_items.models import (
    MenuItemUpdateRequest,
)
import app.menu_items.queries as db_query

menu_item_controller = Blueprint("menu_item_controller", __name__, template_folder="templates")

@menu_item_controller.post("/menu-item/<int:menu_item_id>")
@validate()
def get_menu_item(menu_item_id: int, body: MenuItemUpdateRequest):
    db_query.update_menu_item(menu_item_id, body)
    return body.model_dump_json()
