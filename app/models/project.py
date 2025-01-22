from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    short_description = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(300), nullable=False)
    video_url = db.Column(db.String(300), nullable=True)
    link_url = db.Column(db.String(300), nullable=True)
    languages_used = db.Column(db.String(200), nullable=True)

