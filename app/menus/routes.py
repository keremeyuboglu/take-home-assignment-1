from flask import Blueprint
from flask_pydantic import validate
from app.menus.models import (
    PostMenuRequest,
    DeleteMenuItemFromMenuRequest,
    InsertMenuItemToMenuRequest,
    GetMenuGroupResponse,
    GetMenuItemsResponse,
    GetMenuResponse
)
import app.menus.queries as db_query

menu_controller = Blueprint("menu_controller", __name__, template_folder="templates")

@menu_controller.get("/menu/<int:restaurant_id>")
def get_menu(restaurant_id: int):
    menu = db_query.get_menu_by_restaurant_id(restaurant_id)
    menu_response = GetMenuResponse(
        menu_groups=[
            GetMenuGroupResponse(
                name=x.name,
                sort_order=x.sort_order,
                menu_items=[
                    GetMenuItemsResponse(
                        name=y.name,
                        description=y.description,
                        stock_status=y.stock_status,
                        image=y.image,
                        ranking=y.ranking,
                        price=y.price,
                        calorie=y.calorie,
                    )
                    for y in x.menu_items
                ],
            )
            for x in menu.menu_groups
        ]
    )
    return menu_response.model_dump_json()


@menu_controller.post("/menu/<int:restaurant_id>")
@validate()
def manipulate_menu_item(restaurant_id: int, body: PostMenuRequest):
    if body.type == "DELETE":
        delete_body = DeleteMenuItemFromMenuRequest(**body.model_dump(exclude_none=True))
        db_query.delete_menu_item_from_menu(restaurant_id, delete_body.menu_item_id)
    elif body.type == "INSERT":
        insert_body = InsertMenuItemToMenuRequest(**body.model_dump(exclude_none=True))
        db_query.insert_menu_item_to_menu(restaurant_id, insert_body.menu_item_id)
    return 200


