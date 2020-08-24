from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

#Local
from security import authenticate, identity
from Resources.item_recourse import Item, Items
from Resources.user_recourse import UserRegister, User
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "pedroHernandez"
api = Api(app)
jwt = JWT(app, authenticate, identity) #/auth path 
db.init_app(app)


api.add_resource(Items, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(User, '/user/<string:username>')
api.add_resource(UserRegister, '/register')



if __name__ == "__main__":
    app.run(port=5000, debug=True)