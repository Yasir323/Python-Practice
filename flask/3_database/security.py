from user import User


users = [
	User(1, 'Yasir', 123)
]

username_mapping = {user.username: user for user in users}
userid_mapping = {user.id: user for user in users}


def authenticate(username, password):
	user = User.find_by_username(username)
	if user and user.password == password:
		return user


def identity(payload):
	user_id = payload['identity']
	return User.find_by_id(user_id)
