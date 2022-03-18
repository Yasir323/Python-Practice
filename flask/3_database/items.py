from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


class Item(Resource):
	
	parser = reqparse.RequestParser()
	parser.add_argument(
		'price',
		type=float,
		required=True,
		help="This field cannot be left blank."
	)

	@classmethod
	def find_by_name(cls, name):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()
		query = "SELECT * FROM items WHERE name=?;"
		result = cursor.execute(query, (name,))
		row = result.fetchone()
		cursor.close()
		connection.close()

		if row:
			return {'item': {'name': row[0], 'price': row[1]}}

	@classmethod
	def insert(cls, item):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()
		query = "INSERT INTO items VALUES (?, ?);"
		result = cursor.execute(query, (item['name'], item['price']))
		# row = result.fetchone()
		connection.commit()
		cursor.close()
		connection.close()

	@classmethod
	def update(cls, item):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()
		query = "UPDATE items SET price=? WHERE name=?;"
		result = cursor.execute(query, (item['price'], item['name']))
		num_rows = cursor.rowcount
		connection.commit()
		cursor.close()
		connection.close()
		if num_rows == 0:
			raise NotImplementedError

	@jwt_required()
	def get(self, name):
		item = self.find_by_name(name)
		if item:
			return item
		return {'message': "Item not found."}, 404

	def post(self, name):
		if self.find_by_name(name):
			return {'message': f"An item with name {name} already exists."}, 400
		data = Item.parser.parse_args()
		item = {'name': name, 'price': data['price']}
		try:
			self.insert(item)
		except:
			return {'message': "An error occurred."}, 500
		return item, 201

	def delete(self, name):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()
		query = "DELETE FROM items WHERE name=?;"
		cursor.execute(query, (name,))
		connection.commit()
		num_rows = cursor.rowcount
		print(num_rows)
		cursor.close()
		connection.close()
		if num_rows != 0:
			return {'message': "Item deleted"}
		print(num_rows)
		return {'message': "Item not found"}, 404

	def put(self, name):
		data = Item.parser.parse_args()
		item = self.find_by_name(name)
		updated_item = {'name': name, 'price': data['price']}
		if not item:
			try:
				self.insert(updated_item)
			except:
				return {'message': "Could not insert."}, 500
		else:
			try:
				self.update(updated_item)
			except:
				return {'message': "Could not update."}, 500
		return updated_item


class ItemList(Resource):

	def get(self):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()
		query = "SELECT * FROM items;"
		cursor.execute(query)
		result = cursor.fetchall()
		cursor.close()
		connection.close()
		items = []
		for row in result:
			items.append(row)
		return {'item': items}
