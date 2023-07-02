from app import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON


class Post(db.Model):
	__tablename__ = 'posts'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255), nullable=False)
	image_url = db.Column(db.String(255), nullable=True)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	content = db.Column(db.Text, nullable=False)

	def __repr__(self):
		return '<Post {}>'.format(self.title)
