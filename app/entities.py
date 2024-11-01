from .database import db
from typing import List, Optional
from datetime import datetime
from sqlalchemy import Table, ForeignKey, Column, DateTime, delete, update, insert
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column


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
    