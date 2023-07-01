from . import db
from flask_sqlalchemy import SQLAlchemy

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    image_file = db.Column(db.String(120), nullable=True)
