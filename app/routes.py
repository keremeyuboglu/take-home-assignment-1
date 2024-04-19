from flask import Blueprint, render_template, abort
from flask_pydantic import validate
from .models import *
from .queries import *

menu_controller = Blueprint('menu_controller', __name__, template_folder='templates')

@menu_controller.get('/menu/<int:restaurant_id>')
def get_menu(restaurant_id: int):
    menu = get_menu_by_restaurant_id(restaurant_id)
    menu_response = MenuResponse(
        menu_groups=[
            MenuGroupResponse(
                name=x.name,
                sort_order=x.sort_order,
                menu_items=[
                    MenuItemsResponse(
                        name=y.name,
                        description=y.description,
                        stock_status=y.stock_status,
                        image=y.image,
                        ranking=y.ranking,
                        price=y.price,
                        calorie=y.calorie
                    ) for y in x.menu_items
                    ]
                ) for x in menu.menu_groups
            ]
    )
    return menu_response.model_dump_json()



@menu_controller.post('/menu/<int:restaurant_id>')
@validate()
def manipulate_menu_item(restaurant_id: int, body: RequestBodyModel):
    if body.type == "DELETE":
        delete_menu_item(restaurant_id, body)
    elif body.type == "UPDATE":
        update_menu_items(restaurant_id, body)
    elif body.type == "INSERT":
        insert_menu_item(restaurant_id, body)   
    
    return 200
    


@menu_controller.post('/menu-item/<int:menu_item_id>')
@validate()
def get_menu_item(menu_item_id: int, body: MenuItemUpdateRequest):
    update_menu_item(menu_item_id, body)
    return body.model_dump_json()


