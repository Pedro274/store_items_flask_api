from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

#local
from Models.user_model import UserModel


parser = reqparse.RequestParser()
parser.add_argument('password',
                    type=str,
                    required=True,
                    help="username field can not be empty")

class User(Resource):
    def get(self, username):
        user = UserModel.find_user_by_username(username)
        if user:
            return user.json()
        return {'message': 'user not found'}, 404


class UserRegister(Resource):
    def post(self):
        parser.add_argument('username',
                    type=str,
                    required=True,
                    help="username field can not be empty")
        args = parser.parse_args()
        user = UserModel.find_user_by_username(args['username'])
        if user == None:
            new_user = UserModel(**args)
            new_user.save_to_db()
            return {'message': 'User registed successfully'}
        return {'message': 'User already exists'}



