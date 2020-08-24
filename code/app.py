from flask import Flask
from flask_jwt import JWT
from flask_restful import Api


#Local
from security import authenticate, identity
from db import db

app = Flask(__name__)
api = Api(app)
app.secret_key = "pedroHernandez"
jwt = JWT(app, authenticate, identity) #/auth path 
db.init_app(app)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')










if __name__ == "__main__":
    app.run(port=5000, debug=True)