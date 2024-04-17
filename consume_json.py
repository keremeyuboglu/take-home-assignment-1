import json

file_name = 'sample_data.json'

with open(file_name, 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)
    menu_items = data["menu_item_map"]
    print(menu_items["148142"])
    # for menu_item in menu_items:
    #     menu_item = MenuItem(
    #     id=item_data["id"],
    #     name=item_data["name"],
    #     description=item_data["description"],
    #     stock_status=item_data["stock_status"],
    #     restaurant_id=item_data["restaurant_id"],
    #     image=item_data["image"],
    #     ranking=item_data["ranking"],
    #     price=item_data["price"],
    #     calorie=item_data["calorie"]
    # )
