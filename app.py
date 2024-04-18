from flask import Flask, jsonify
from util import get_seed_data, convert_keys_to_pascal_case
from db import db, Base
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Table, ForeignKey, Column, DateTime, delete, update, insert
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel
from flask_pydantic import validate
from typing import Optional, List

  
  
class MenuItemsResponse(BaseModel):
    name: str
    description: Optional[str]
    stock_status: str
    image: Optional[str]
    ranking: Optional[int]
    price: float
    calorie: Optional[float]
    
class MenuGroupResponse(BaseModel):
    name: str
    sort_order: int
    menu_items: List[MenuItemsResponse]  

class MenuResponse(BaseModel):
    menu_groups: List[MenuGroupResponse]

def check_if_non_seeded_db():
    with app.app_context():
        try:
            item = db.session.execute(db.select(Restaurant)).one()
            return False
        except Exception as e:
            print(e)
            return True

def seed_db(data_dict):
    with app.app_context():
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
    restaurant_id: Mapped[int] = mapped_column("RestaurantId", ForeignKey("Restaurant.Id"))
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
    menu_id : Mapped[int] = mapped_column("MenuId", ForeignKey("Menu.Id"))
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
    
class Menu(db.Model):
    __tablename__ = "Menu"
    
    id: Mapped[int] = mapped_column("Id", primary_key=True, unique=True)
    restaurant_id : Mapped[int] = mapped_column("RestaurantId", ForeignKey("Restaurant.Id"))
    created_at: Mapped[datetime] = mapped_column("CreatedAt", DateTime, default=datetime.now())
    menu_groups: Mapped[List["MenuGroup"]] = relationship(
        # "MenuGroup",
        # back_populates="menu_groups"
    )
    
class Restaurant(db.Model):
    __tablename__ = "Restaurant"
    
    id: Mapped[int] = mapped_column("Id", primary_key=True, unique=True)
    name: Mapped[str] = mapped_column("Name")
    menus: Mapped[List["Menu"]] = relationship(
        # "Menu",
        # back_populates="menus"
    )
    


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


@app.get('/menu/<int:restaurant_id>')
def get_menu(restaurant_id: int):
    menu: Menu = db.session.scalars(
        db.select(Menu).filter_by(restaurant_id=restaurant_id).order_by(Menu.created_at.desc()).limit(1)
        ).first()     
      
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


class RequestBodyModel(BaseModel):
    type: str
    id: int
    name: Optional[str] = None
    description: Optional[str] = None
    stock_status: Optional[str] = None
    image: Optional[str] = None
    ranking: Optional[int] = None
    price: Optional[float] = None
    calorie: Optional[float] = None

@app.post('/menu/<int:restaurant_id>')
@validate()
def manipulate_menu_item(restaurant_id: int, body: RequestBodyModel):
    if body.type == "DELETE":
        stmt = delete(MenuItem).where(MenuItem.id == body.id, MenuItem.restaurant_id == restaurant_id)
        db.session.execute(stmt)
        db.session.commit()
    elif body.type == "UPDATE":
        stmt = update(MenuItem).where(MenuItem.id == body.id, MenuItem.restaurant_id == restaurant_id).values(
            body.model_dump(exclude={'type', 'id'})
        )
        db.session.execute(stmt)
        db.session.commit()
        pass
        
    elif body.type == "INSERT":
        stmt = insert(MenuItem).values(
            body.model_dump(exclude={'type', 'id'})
        )
        db.session.execute(stmt)
        db.session.commit()
        pass
    
    return 200
    

@app.get('/menu-item/<int:menu_item_id>')
def get_menu_item(menu_item_id: int):
    return 5

# Menu
# Menu Item
# Restaurant

