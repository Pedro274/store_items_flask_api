from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from Models.item_model import ItemModel
from Models.store_model import StoreModel

class Items(Resource):
    def get(self):
        items = [item.json() for item in ItemModel.get_all_items()]
        return {
            'message': 'These are all the items available in the database ',
            'items': items
        }

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                    type=float,
                    required= True,
                    help='This field cannot be left blank')


    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        self.parser.add_argument('store_id',
                    type=int,
                    required= True,
                    help='This field cannot be left blank')
        args = self.parser.parse_args()

        item = ItemModel.find_by_name(name)
        store = StoreModel.find_by_id(args.store_id)
        if store == None:
            return {'message': 'Store not found check id provided'}, 404
        if item == None:
            new_Item = ItemModel(name, **args)
            new_Item.save_to_db()
            return {
                'message': 'Item was created',
                'item': new_Item.json()
            }
        return {'message': f'item with the name of {name} already exits'}


    def put(self, name):
        args = self.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item:
            item.price = args.get('price', item.price)
            item.save_to_db()
            return {
                'message':'Item was updated',
                'item_updated': item.json()
            }, 202
        return {'message': 'Item not found'}, 404


    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.remove_from_db()
            return {'message': 'Item was deleted'}
        return {'message': 'Item not found'}, 404
