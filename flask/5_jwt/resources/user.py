from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    get_raw_jwt
)
from blacklist import BLACKLIST

_user_parser = reqparse.RequestParser()
_user_parser.add_argument(
    'username',
    type=str,
    required=True,
    help="This field cannot be blank."
)
_user_parser.add_argument(
    'password',
    type=str,
    required=True,
    help="This field cannot be blank."
)


class UserRegister(Resource):

    def post(self):
        data = _user_parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201


class User(Resource):
    
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': "User not found."}, 404
        return user.json()

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': "User not found."}, 404
        user.delete_from_db()
        return {'message': "User deleted."}, 200


class UserLogin(Resource):
    

    @classmethod
    def post(cls):
        # Get the data from parser
        data = _user_parser.parse_args()
        # Find the user in the database
        user = UserModel.find_by_username(data['username'])
        # Check password
        if user and user.password == data['password']:
            # Create access token
            access_token = create_access_token(identity=user.id, fresh=True)
            # Create refresh token
            refresh_token = create_refresh_token(user.id)
            # Return them
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        return {'message': "Invalid credentials."}, 401


class UserLogout(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']  # jti is "JWT ID", a unique identifier for a JWT.
        BLACKLIST.add(jti)
        return {"message": "Successfully logged out"}, 200


class TokenRefresh(Resource):

    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {'access_token': new_token}, 200
