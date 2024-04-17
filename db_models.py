from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
from db import db, Base

menu_group_item_map_table = Table(
    "MenuGroupItemMap",
    Base.metadata,
    Column("MenuGroupId", ForeignKey("MenuGroup.Id"), primary_key = True),
    Column("MenuItemId", ForeignKey("MenuItem.Id"), primary_key = True),
    extend_existing=True
)

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
    calories: Mapped[float] = mapped_column("Calories")
    menu_group_items: Mapped[list["MenuGroup"]] = relationship(
        secondary=menu_group_item_map_table, back_populates="menu_items"
    )
    
class MenuGroup(db.Model):
    __tablename__ = "MenuGroup"
    
    id: Mapped[int] = mapped_column("Id", primary_key=True, unique=True)
    name: Mapped[str] = mapped_column("Name")
    sort_order: Mapped[int] = mapped_column("SortOrder")
    menu_items: Mapped[list["MenuItem"]] = relationship(
        secondary=menu_group_item_map_table, back_populates="menu_group_items"
    )

    
class MenuGroupItemMap(db.Model):
    __tablename__ = "MenuGroupItemMap"
    __table_args__ = {'extend_existing': True}
    
    menu_group_id: Mapped[int] = mapped_column("MenuGroupId", primary_key=True, unique=True)
    menu_item_id: Mapped[int] = mapped_column("MenuItemId", primary_key=True, unique=True)