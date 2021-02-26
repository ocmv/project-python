import datetime

from . import db

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True, nullable=False)
	password = db.Column(db.String(93), nullable=False)
	email = db.Column(db.String(100), unique=True, nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.datetime.now())

	@classmethod
	def create_element(cls, username, password, email):
		user = User(username=username, password=password, email=email)
		db.session.add(user)
		db.session.commit()

		return user

	