# Contains endpoints for Items Api's

# Marshmallow can be used for validation in incoming data
# so we cannot use it for checking if item already exist
import uuid
from flask.views import MethodView
from flask import Flask, request
from flask_smorest import abort, Blueprint
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items",__name__, description="Items information")

@blp.route("/item")
class ItemList(MethodView):

    @blp.response(200, ItemSchema(many=True))
    def get(self):
        # return {"items": list(items.values())}
        # due to above blp marshmallow business it will automatically change into a list
        return items.values()

    @blp.arguments(ItemSchema)
    @blp.response(201,ItemSchema)
    def post(self, item_data):
        # below written item_data can be accessed with marshmallow as written above
        # it is checked for validation and then sent in here, we dont need to fetch it it's already
        # fetched and checked
        # item_data = request.get_json()
        # if "price" not in item_data or "name" not in item_data or "store_id" not in item_data:
        #     abort(400, message="Ensure, price, name and store_id included in json payload")

        for item in items.values():
            if item_data["name"] == item["name"] or item_data["store_id"] == items["store_id"]:
                abort(400, message="Item Already Exist")

        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item
        return item, 201


@blp.route("/item/<string:item_id>")
class Item(MethodView):

    @blp.response(200,ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted"}
        except KeyError:
            abort(404, message="Item not found")

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        # item_data = request.get_json()
        #
        # if "price" not in item_data or "name" not in item_data:
        #     abort(404, message="Bad request, ensure all info is there in payload")
        try:
            item = items[item_id]
            # dictionary inplace update method
            item |= item_data
            return item
        except KeyError:
            abort(404, message="Item not found")