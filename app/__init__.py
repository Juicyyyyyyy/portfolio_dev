import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
admin = Admin(template_mode='bootstrap3')

# Import all models so they are registered with SQLAlchemy
from app.models.experience import Experience
from app.models.post import Post
from app.models.project import Project
from app.models.skill import Skill
from app.models.skill_category import Category

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)

    with app.app_context():
        try:
            db.create_all()
            print("Database tables created successfully")
        except Exception as e:
            print(f"Error creating tables: {e}")

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
