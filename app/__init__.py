from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')

app.config['SECRET_KEY'] = os.getenv('SENDGRID_API_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('JAWSDB_MARIA_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME=os.getenv('SENDGRID_USERNAME'),
    MAIL_PASSWORD=os.getenv('SENDGRID_PASSWORD'),
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

admin = Admin(app, name='myadmin', template_mode='bootstrap3')

from app.models.post import Post
from app.models.project import Project
from app.models.company import Experience
from app.models.skill import Skill
from app.models.skill_category import Category

admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Project, db.session))
admin.add_view(ModelView(Experience, db.session))
admin.add_view(ModelView(Skill, db.session))
admin.add_view(ModelView(Category, db.session))

from app import routes
