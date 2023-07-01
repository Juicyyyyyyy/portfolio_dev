from app import db


class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), nullable=False)
	order = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return '<Category %r>' % self.name
