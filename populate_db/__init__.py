from flask import Flask

from app import db
from app import Project, Category, Experience, Skill, Post
from datetime import datetime
import os


# Vide toutes les tables de la database
def kill_db():
	meta = db.metadata
	for table in reversed(meta.sorted_tables):
		db.session.execute(table.delete())
	db.session.commit()


def create_app():
	# Create the Flask application
	app = Flask(__name__)

	# Set the configuration for the application
	app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('JAWSDB_MARIA_URL')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	# Initialize SQLAlchemy with this application
	db.init_app(app)

	return app


app = create_app()
