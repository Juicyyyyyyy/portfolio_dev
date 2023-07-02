from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:oJiDWXpYXRZq8bRxFpwR@localhost:5432/portfolio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

admin = Admin(app, name='myadmin', template_mode='bootstrap3')

from app.models.post import Post
from app.models.project import Project
from app.models.company import Experience
from app.models.skill import Skill
from app.models.skill_category import Category
from app.models.post import Post

admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Project, db.session))
admin.add_view(ModelView(Experience, db.session))
admin.add_view(ModelView(Skill, db.session))

from app import routes
