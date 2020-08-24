from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from Models.item_model import ItemModel

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
        item = ItemModel.find_by_name(name)
        if item == None:
            args = self.parser.parse_args()
            new_Item = ItemModel(name, args['price'])
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
            item['price'] = args.get('price', item['price'])
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
