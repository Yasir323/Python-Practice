from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
import sqlite3


class Item(Resource):
	
	parser = reqparse.RequestParser()
	parser.add_argument(
		'price',
		type=float,
		required=True,
		help="This field cannot be left blank."
	)
	parser.add_argument(
		'store_id',
		type=int,
		required=True,
		help="Every item needs a sotre ID."
	)

	@jwt_required()
	def get(self, name):
		item = ItemModel.find_by_name(name)
		if item:
			return item.json()
		return {'message': "Item not found."}, 404

	def post(self, name):
		if ItemModel.find_by_name(name):
			return {'message': f"An item with name {name} already exists."}, 400
		data = Item.parser.parse_args()
		item = ItemModel(name, **data)
		try:
			item.upsert()
		except:
			return {'message': "An error occurred."}, 500
		return item.json(), 201

	def delete(self, name):
		item = ItemModel.find_by_name(name)
		if item:
			item.delete()
		return {'message': "Item deleted successfully."}

	def put(self, name):
		data = Item.parser.parse_args()
		item = ItemModel.find_by_name(name)
		if not item:
			item = ItemModel(name, **data)
		else:
			item.price = data['price']
			item.store_id = data['store_id']
		item.upsert()
		return item.json()


class ItemList(Resource):

	def get(self):
		return {'items': [item.json() for item in ItemModel.query.all()]}
		