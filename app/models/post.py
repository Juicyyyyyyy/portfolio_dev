from app import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON
import markdown


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    excerpt = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    header = db.Column(db.String(200), nullable=False)
    introduction = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    conclusion = db.Column(db.String(200), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image_url = db.Column(db.String(250), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

    def body_markdown(self):
        return markdown.markdown(self.body)


