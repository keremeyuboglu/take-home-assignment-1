from flask import Flask, jsonify
from util import get_seed_data, convert_keys_to_pascal_case
from db import db, Base
from flask import Flask
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column


def check_if_non_seeded_db():
    with app.app_context():
        try:
            item = db.session.execute(db.select(MenuItem)).scalar_one()
            return False
        except:
            return True

def seed_db(data_dict):
    with app.app_context():
        menu_groups = data_dict["menu_group_map"]
        menu_items = data_dict["menu_item_map"]
        menu_group_mappings: dict = data_dict["menu_group_menu_item_lookup"]

        for menu_group_key in menu_groups:
            menu_group_attributes=menu_groups[menu_group_key]
            menu_group_entity = MenuGroup(**menu_group_attributes)
            db.session.add(menu_group_entity)

        for menu_item_key in menu_items:
            menu_item_attributes=menu_items[menu_item_key]
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
                flg = 5
        
        db.session.commit()
                
        best_flg = 5

  


# menu_group_item_map_table = Table(
#     "MenuGroupItemMap",
#     Base.metadata,
#     Column("MenuGroupId", ForeignKey("MenuGroup.Id"), primary_key = True),
#     Column("MenuItemId", ForeignKey("MenuItem.Id"), primary_key = True),
#     extend_existing=True
# )

from typing import List

class MenuItem(db.Model):
    __tablename__ = "MenuItem"
    
    id: Mapped[int] = mapped_column("Id", primary_key=True, unique=True)
    name: Mapped[str] = mapped_column("Name", unique=True)
    description: Mapped[str] = mapped_column("Description")
    stock_status: Mapped[str] = mapped_column("StockStatus")
    restaurant_id: Mapped[int] = mapped_column("RestaurantId")
    image: Mapped[str] = mapped_column("Image")
    ranking: Mapped[int] = mapped_column("Ranking")
    price: Mapped[float] = mapped_column("Price")
    calorie: Mapped[float] = mapped_column("Calorie")
    menu_group_items: Mapped[List["MenuGroup"]] = relationship(
        "MenuGroup",
        secondary="MenuGroupItemMap", 
        back_populates="menu_items"
    )
    
class MenuGroup(db.Model):
    __tablename__ = "MenuGroup"
    
    id: Mapped[int] = mapped_column("Id", primary_key=True, unique=True)
    name: Mapped[str] = mapped_column("Name")
    sort_order: Mapped[int] = mapped_column("SortOrder")
    menu_items: Mapped[List["MenuItem"]] = relationship(
        "MenuItem",
        secondary="MenuGroupItemMap", 
        back_populates="menu_group_items"
    )

    
class MenuGroupItemMap(db.Model):
    __tablename__ = "MenuGroupItemMap"
    __table_args__ = {'extend_existing': True}
    
    menu_group_id: Mapped[int] = mapped_column("MenuGroupId", ForeignKey("MenuGroup.Id"), primary_key=True, unique=True)
    menu_item_id: Mapped[int] = mapped_column("MenuItemId", ForeignKey("MenuItem.Id"), primary_key=True, unique=True)


database_credentials = {
    'dbname': 'Unplug',
    'user': 'postgres',
    'password': '123',
    'host': 'localhost',
    'port': '5432'
}

app = Flask(__name__)
connection_string = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}".format(**database_credentials)
app.config["SQLALCHEMY_DATABASE_URI"] = connection_string

db.init_app(app)

if check_if_non_seeded_db():
    seed_data = get_seed_data()
    # seed_data = convert_keys_to_pascal_case(seed_data)
    seed_db(seed_data)


@app.get('/')
def hello():
    file_name = 'sample_data.json'
    menu_item = None

    # with open(file_name, 'r') as file:
    #     # Load the JSON data from the file
    #     data = json.load(file)
    #     menu_items = data["menu_item_map"]
    #     item_data = menu_items["148142"]
        
    # menu_item = MenuItem(
    #     id=item_data["id"],
    #     name=item_data["name"],
    #     description=item_data["description"],
    #     stock_status=item_data["stock_status"],
    #     restaurant_id=item_data["restaurant_id"],
    #     image=item_data["image"],
    #     ranking=item_data["ranking"],
    #     price=item_data["price"],
    #     calories=item_data["calorie"]
    # )
    # db.session.add(menu_item)
    # db.session.commit()
    return 'Hello, World!'

@app.get('/menu/<restaurant_id>')
def get_menu(restaurant_id: int):
    # db.get_or_404(MenuItem)
    # user = db.one_or_404(
    #     db.select(MenuItem).filter_by(id=restaurant_id)
    # )
    # return jsonify(user)
    return 5

@app.post('/menu/<restaurant_id>')
def create_menu(restaurant_id: int):
    return 5

@app.get('/menu-item/<menu_item_id>')
def get_menu_item(menu_item_id: int):
    return 5

# Menu
# Menu Item
# Restaurant

