from app import db  # assuming your Flask app is named app

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    short_description = db.Column(db. String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(255), nullable=False)
    img_src = db.Column(db.String(255), nullable=False)
    languages_used = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Experience %r>' % self.name
