from flask import Blueprint
from flask_pydantic import validate
from app.models import (
    GetMenuGroupResponse,
    GetMenuItemsResponse,
    MenuItemUpdateRequest,
    GetMenuResponse,
    PostMenuRequest,
    DeleteMenuRequest,
    InsertMenuRequest,
    UpdateMenuRequest
)
import app.queries as db_query

menu_controller = Blueprint("menu_controller", __name__, template_folder="templates")

@menu_controller.get("/")
def hello_world():
    return "Hello World!"

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
        delete_body = DeleteMenuRequest(**body.model_dump(exclude_none=True))
        db_query.delete_menu_item(restaurant_id, delete_body.id)
    elif body.type == "UPDATE":
        update_body = UpdateMenuRequest(**body.model_dump(exclude_none=True))
        db_query.update_menu_items(restaurant_id, update_body)
    elif body.type == "INSERT":
        insert_body = InsertMenuRequest(**body.model_dump(exclude_none=True))
        db_query.insert_menu_item(restaurant_id, insert_body)
    return 200


@menu_controller.post("/menu-item/<int:menu_item_id>")
@validate()
def get_menu_item(menu_item_id: int, body: MenuItemUpdateRequest):
    db_query.update_menu_item(menu_item_id, body)
    return body.model_dump_json()
