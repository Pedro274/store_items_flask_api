from db import db

class StoreModel(db.Model):
    __tablename__= 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    
    #relationship
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel')
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def json(self):
        return {'name': self.name, "id": self.id, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def get_all_stores(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def remove_from_db(self):
        db.session.delete(self)
        db.session.commit()

