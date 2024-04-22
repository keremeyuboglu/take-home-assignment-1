from flask import Blueprint, abort
from app.menu_items.models import (
    MenuItemUpdateRequestSchema,
    MenuItemUpdateResponseSchema
)
import app.menu_items.queries as db_query
from apifairy import body, response, other_responses

menu_item_controller = Blueprint("menu_item_controller", __name__, template_folder="templates")

@menu_item_controller.post("/menu-item/<menu_item_id>")
@body(MenuItemUpdateRequestSchema)
@response(MenuItemUpdateResponseSchema, 200)
@other_responses({400: 'Update cannot be processed'})
def update_menu_item(body: MenuItemUpdateRequestSchema, menu_item_id: int):
    try:
        updated_menu_item = db_query.update_menu_item(menu_item_id, body)
    except Exception as e:
        return abort(400)
    return updated_menu_item
