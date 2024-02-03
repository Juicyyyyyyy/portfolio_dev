from app import db
from datetime import datetime
import markdown


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image_url = db.Column(db.String(250))

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"