# Contains all the code of Store Api's

import uuid
from flask.views import MethodView
from flask import Flask, request
from flask_smorest import abort, Blueprint
from schemas import StoreSchema
from models import StoreModel
from db import db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

blp = Blueprint("Stores",__name__, description="Stores information")


@blp.route("/store")
class StoreList(MethodView):

    @blp.response(200,StoreSchema(many=True))
    def get(self):
        # return stores.values()
        return StoreModel.query.all()

    @blp.arguments(StoreSchema)
    @blp.response(201,StoreSchema)
    def post(self, store_data):
        # store_data = request.get_json()
        # if "name" not in store_data:
        #     abort(400, message="Ensure, name is included in json payload")

        # for store in stores.values():
        #     if store_data["name"] == store["name"]:
        #         abort(400, message="Store Already Exist")

        # store_id = uuid.uuid4().hex
        # # it changes the form of data is required format **
        # store = {**store_data, "id": store_id}
        # stores[store_id] = store
        # return store, 201
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Item Already Exist")
        except SQLAlchemyError:
            abort(500, "An error occurred while adding")


@blp.route("/store/<string:store_id>")
class Store(MethodView):

    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store

    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "Store Deleted"}