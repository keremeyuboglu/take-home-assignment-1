from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db_models import * 
from db import db
from sqlalchemy.orm import DeclarativeBase


def check_if_non_seeded_db():
  item = db.session.execute(db.select(MenuItem)).scalar_one()
  if item:
    return True
  return False

def seed_db(data_dict):
  menu_groups = data_dict["MenuGroupMap"]
  menu_items = data_dict["MenuItemMap"]
  menu_group_mappings: dict = data_dict["MenuGroupItemLookup"]
  
  for menu_group in menu_groups:
    menu_group_entity = MenuGroup(
      id=menu_group["id"],
      name=menu_group["name"],
      sort_order=menu_group["sort_order"],
    )
    db.session.add(menu_group_entity)
    
  for menu_item in menu_items:
    menu_item_entity = MenuItem(
        id=menu_item["id"],
        name=menu_item["name"],
        description=menu_item["description"],
        stock_status=menu_item["stock_status"],
        restaurant_id=menu_item["restaurant_id"],
        image=menu_item["image"],
        ranking=menu_item["ranking"],
        price=menu_item["price"],
        calories=menu_item["calorie"]
    )
    db.session.add(menu_item_entity)
  
  for menu_group_mapping in menu_group_mappings:
    menu_group_mapping
    menu_group_mapping_item = MenuGroupItemMap(
      
    )
    db.session.execute(menu_group_item_map_table)
    menu_group_item_map_table()
  