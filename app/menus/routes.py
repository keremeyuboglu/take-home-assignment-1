from flask import Blueprint, abort
from app.menus.models import (
    MenuSchema,
    PostMenuSchema
)
import app.menus.queries as db_query
from apifairy import body, response, other_responses


menu_controller = Blueprint("menu_controller", __name__, template_folder="templates")

@menu_controller.get("/menu/<int:restaurant_id>")
@response(MenuSchema, 200)
@other_responses({400: 'Request cannot be processed',
                  404: "Menu is not found"})
def get_latest_menu(restaurant_id: int):
    """Get the latest updated menu by restaurant id"""
    try:
        menu = db_query.get_menu_by_restaurant_id(restaurant_id)
    except Exception as e:
        abort(400)    
    return menu or abort(404)


@menu_controller.post("/menu/<int:restaurant_id>")
@body(PostMenuSchema)
@response(MenuSchema, 200)
@other_responses({400: 'Update operation cannot be processed'})
def manipulate_menu_item(body: PostMenuSchema, restaurant_id: int):
    """Insert or delete menu item from menu by menu and restaurant ids"""
    try:
        if body["type"] == "DELETE":
            db_query.delete_menu_item_from_menu(restaurant_id, body["menu_item_id"])
        elif body["type"] == "INSERT":
            db_query.insert_menu_item_to_menu(restaurant_id, body["menu_item_id"])
    except Exception as e:
        abort(400)
    return 200


