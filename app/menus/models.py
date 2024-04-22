from marshmallow import Schema, fields, validate
from app import ma
from app.entities import MenuItem, Menu, MenuGroup
    
class MenuItemSchema(ma.SQLAlchemySchema):
    class Meta:
        model = MenuItem
        ordered = True
        description = 'This schema represents a menu item.'
    # Depending on use case ID shouldn't be returned but
    # for faster demoing purposes I added it
    id = fields.Str(allow_none=True)
    name = fields.Str(allow_none=True)
    description = fields.Str(allow_none=True)
    stock_status = fields.Str(allow_none=True)
    image = fields.Str(allow_none=True)
    ranking = fields.Int(allow_none=True)
    price = fields.Float(allow_none=True)
    calorie = fields.Float(allow_none=True)
    
class MenuGroupSchema(ma.SQLAlchemySchema):
    class Meta:
        model = MenuGroup
        ordered = True
        description = 'This schema represents a menu group.'
    name = fields.String(required=True)
    sort_order = fields.Integer(required=True)
    menu_items = fields.List(fields.Nested(MenuItemSchema)) 
    
class MenuSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Menu
        ordered = True
        description = 'This schema represents a menu.'
    menu_groups = fields.List(fields.Nested(MenuGroupSchema))
    

class PostMenuSchema(Schema):
    class Meta:
        description = 'This schema represents a menu item id.'
    type = fields.String(required=True, validate=validate.OneOf(["INSERT", "DELETE"]))
    menu_item_id = fields.Integer(required=True)
    