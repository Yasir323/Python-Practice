import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegistration(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument(
		'username',
		type=str,
		required=True,
		help="This field cannot be left blank."
	)
	parser.add_argument(
		'password',
		type=str,
		required=True,
		help="This field cannot be left blank."
	)


	def post(self):
		data = UserRegistration.parser.parse_args()
		if UserModel.find_by_username(data['username']):
			return {'message': "Username already taken."}, 400

		user = UserModel(**data)
		user.upsert()
		
		return {'message': "User created successfully."}, 201
