from marshmallow import Schema, fields, validate
from app import ma
from app.entities import MenuItem

class MenuItemUpdateRequestSchema(Schema):
    name = fields.Str(allow_none=True)
    description = fields.Str(allow_none=True)
    stock_status = fields.Str(allow_none=True)
    image = fields.Str(allow_none=True)
    ranking = fields.Int(validate=validate.Range(min=1), allow_none=True)
    price = fields.Float(validate=validate.Range(min=0, min_inclusive=False), allow_none=True)
    calorie = fields.Float(validate=validate.Range(min=0, min_inclusive=False), allow_none=True)
    

class MenuItemUpdateResponseSchema(ma.SQLAlchemySchema):
    class Meta:
        model = MenuItem
        ordered = True
        description = 'This schema represents a menu item.'
        
    name = fields.String(required=True)
    description = fields.String(allow_none=True)
    stock_status = fields.String(allow_none=True)
    image = fields.String(allow_none=True)
    ranking = fields.Integer(allow_none=True)
    price = fields.Float(allow_none=True)
    calorie = fields.Float(allow_none=True)
