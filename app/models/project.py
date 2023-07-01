from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(300), nullable=False)
    video_url = db.Column(db.String(300), nullable=True)
    link_url = db.Column(db.String(300), nullable=True)
    languages_used = db.Column(db.String(200), nullable=True)

    def __init__(self, title, description, image_url, video_url, link_url, languages_used):
        self.title = title
        self.description = description
        self.image_url = image_url
        self.video_url = video_url
        self.link_url = link_url
        self.languages_used = languages_used
