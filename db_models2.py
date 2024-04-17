from decimal import Decimal

from sqlalchemy import Column, ForeignKeyConstraint, Integer, MetaData, Numeric, PrimaryKeyConstraint, Table, Text, UniqueConstraint

t_MenuGroup = Table(
    'MenuGroup', metadata,
    Column('Id', Integer, nullable=False),
    Column('Name', Text),
    Column('SortOrder', Integer),
    UniqueConstraint('Id', name='MenuGroup_Id_key')
)


t_MenuItem = Table(
    'MenuItem', metadata,
    Column('Id', Integer, nullable=False),
    Column('Name', Text),
    Column('Description', Text),
    Column('StockStatus', Text),
    Column('RestaurantId', Integer),
    Column('Image', Text),
    Column('Ranking', Integer),
    Column('Price', Numeric),
    Column('Calories', Numeric),
    UniqueConstraint('Id', name='MenuItem_Id_key')
)


t_MenuGroupItemMap = Table(
    'MenuGroupItemMap', metadata,
    Column('MenuGroupId', Integer, primary_key=True, nullable=False),
    Column('MenuItemId', Integer, primary_key=True, nullable=False),
    ForeignKeyConstraint(['MenuGroupId'], ['MenuGroup.Id'], ondelete='CASCADE', onupdate='CASCADE', name='MenuGroupItemMap_MenuGroupId_fkey'),
    ForeignKeyConstraint(['MenuItemId'], ['MenuItem.Id'], name='MenuGroupItemMap_MenuItemId_fkey'),
    PrimaryKeyConstraint('MenuGroupId', 'MenuItemId', name='MenuGroupItemMap_pkey')
)
