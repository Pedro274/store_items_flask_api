from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from Models.store_model import StoreModel
from Models.user_model import UserModel

class Stores(Resource):
    def get(self):
        return {
            'message' : 'These are the store available',
            'stores' : [store.json() for store in StoreModel.get_all_stores()]
        }

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        request = reqparse.RequestParser()
        request.add_argument("user_id", type= int, help="need user id to create store")
        data = request.parse_args()

        store = StoreModel.find_by_name(name)
        user = UserModel.find_user_by_id(data.user_id)

        if user == None:
            return {'message': 'User not found check id provided'}, 404
        if store == None:
            new_store = StoreModel(name, **data)
            new_store.save_to_db()
            return {'message': 'New store was created'},201
        return {'message': 'store already exists'}
