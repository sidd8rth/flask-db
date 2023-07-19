from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    # helps to see item associated with it 
    # lazy=dynamic means it is not auto fetch
    # as it might add some overhead
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")