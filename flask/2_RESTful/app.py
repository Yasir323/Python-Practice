from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'SECRET_KEY'
api = Api(app)
jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):
	
	parser = reqparse.RequestParser()
	parser.add_argument(
		'price',
		type=float,
		required=True,
		help="This field cannot be left blank."
	)

	@jwt_required()
	def get(self, name):
		item = next(filter(lambda x: x['name'] == name, items), None)
		return {'item': item}, 200 if item else 404

	def post(self, name):
		if next(filter(lambda x: x['name'] == name, items), None):
			return {'message': f"An item with name {name} already exists."}, 400
		data = Item.parser.parse_args()
		# data = request.get_json()
		item = {'name': name, 'price': data['price']}
		items.append(item)
		return item, 201

	def delete(self, name):
		global items
		# items = list(filter(lambda x: x['name'] != name, items))
		for i in range(len(items)):
			if items[i]['name'] == name:
				items.pop(i)
				return {'message': "Items deleted."}
		return {'message': "Item not found"}, 404

	def put(self, name):
		# Parsing request
		data = Item.parser.parse_args()

		# data = request.get_json()  # Withoput parsing payload
		item = next(filter(lambda x: x['name'] == name, items), None)
		if not item:
			item = {
				'name': name,
				'price': data['price']
			}
			items.append(item)
		else:
			item.update(data)
		return item


class ItemList(Resource):

	def get(self):
		return {'item': items}

api.add_resource(ItemList, '/item')
api.add_resource(Item, '/item/<string:name>')
app.run(debug=True)
