from db import db

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False, unique=True)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"),unique=False, nullable=False)
    # this below line defines a relationship
    # if helps us to access the store model related to that store_id that we used above 
    # one endpoint of a relationship
     # MyItem.store is the store model associated with that item
    store = db.relationship("StoreModel", back_populates='items')