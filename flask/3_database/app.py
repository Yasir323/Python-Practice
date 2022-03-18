from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from user import UserRegistration
from items import Item, ItemList

app = Flask(__name__)
app.secret_key = 'SECRET_KEY'
api = Api(app)
jwt = JWT(app, authenticate, identity)

api.add_resource(ItemList, '/item')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegistration, '/register')

if __name__ == '__main__':
	app.run(debug=True)
