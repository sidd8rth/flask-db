# For validations Stuff
# we define what is required while requesting or sending data here
# It will be used later in final python coding files for validation

from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    # dump_only meaning only for returning data
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    # store_id = fields.Str(required=True)

class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


# this plain schema thing is done here because if we would have kept normal schema then
# in that case we would be in a loop or deadloack situation as both of them would have called 
# each other to update

class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)