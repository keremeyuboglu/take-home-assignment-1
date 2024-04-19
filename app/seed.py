  
from app.entities import *
from app.models import *
from app.util import get_seed_data

def seed_data_if_unseeded(app):
    with app.app_context():
        try:
            db.session.execute(db.select(Restaurant)).one()
            return
        except Exception as e:
            seed_db(get_seed_data())
            return True

def seed_db(data_dict):
    restaurant = Restaurant(
        name="TestRestaurant"
    )
    db.session.add(restaurant)
    db.session.commit()
    
    menu = Menu(
        restaurant_id = restaurant.id
    )
    
    db.session.add(menu)
    db.session.commit()
    
    menu_groups = data_dict["menu_group_map"]
    menu_items = data_dict["menu_item_map"]
    menu_group_mappings: dict = data_dict["menu_group_menu_item_lookup"]

    for menu_group_key in menu_groups:
        menu_group_attributes=menu_groups[menu_group_key]
        menu_group_attributes["menu_id"] = menu.id
        menu_group_entity = MenuGroup(**menu_group_attributes)
        db.session.add(menu_group_entity)
    
    db.session.commit()

    for menu_item_key in menu_items:
        menu_item_attributes=menu_items[menu_item_key]
        menu_item_attributes["restaurant_id"] = restaurant.id
        menu_item_entity = MenuItem(**menu_item_attributes)
        db.session.add(menu_item_entity)

    db.session.commit()
    
    for menu_group_id in menu_group_mappings:
        menu_item_ids = menu_group_mappings[menu_group_id]
        for menu_item_id in menu_item_ids:
            menu_map = MenuGroupItemMap(
                menu_group_id=menu_group_id,
                menu_item_id=menu_item_id
            )
            db.session.add(menu_map)
            # insert_statement = menu_group_item_map_table.insert().values(
            #     MenuGroupId=menu_group_id, MenuItemId=menu_item_id
            # )
            # db.session.execute(insert_statement)
    
    db.session.commit()