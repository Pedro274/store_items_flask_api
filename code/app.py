from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

#Local
from Resources.item_recourse import Item, Items
from Resources.user_recourse import UserRegister, User
from Resources.store_resources import Store, Stores
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = "pedro"
api = Api(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Items, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(User, '/user/<string:username>')
api.add_resource(UserRegister, '/register')
api.add_resource(Stores, '/stores')
api.add_resource(Store, '/store/<string:name>')


if __name__ == "__main__":
    app.run(port=5000, debug=True)